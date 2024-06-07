# ch4_13_sales_analysis

## 매출 분석

이번 장에서는 olist 데이터 셋을 기준으로 간단한 매출 분석을 해보겠습니다. 매출 분석이라고 해봐야 일별, 주별, 월별 매출 추이를 집계하여 그래프로 시각화 하는 정도입니다. 

### 테이블 준비

orders 테이블과 order_payments 테이블을 만들고, 데이터를 부어줍니다.

![Untitled](ch4_13_sales_analysis%208489e112db2b433b90fed7d37fd18460/Untitled.png)

![Untitled](ch4_13_sales_analysis%208489e112db2b433b90fed7d37fd18460/Untitled%201.png)

### 인덱스 생성

그 다음, orders.order_id 컬럼과 order_payments.order_id를 기준으로 JOIN을 수행할 예정입니다. orders.order_id는 primary key로 지정되어 있으므로 인덱스가 자동으로 걸려있지만, order_payments.order_id는 그렇지 않습니다. 따라서 인덱스를 생성해줍니다.

```sql
CREATE INDEX idx_order_payments_order_id ON order_payments(order_id);
```

### 일별 매출 집계

시작은 가볍게 2017년 1월에 발생한 매출액을 일별로 집계하는 쿼리를 짜보겠습니다. 그러려면 매출액이 발생한 시간과 매출액 데이터를 읽어와야 합니다. 

```sql
SELECT
	orders.order_purchase_timestamp,
	order_payments.payment_value
FROM
	orders
LEFT JOIN order_payments
ON order_payments.order_id=orders.order_id
WHERE
	orders.order_purchase_timestamp >= "2017-01-01"
    AND orders.order_purchase_timestamp <= "2017-01-31"
```

![Untitled](ch4_13_sales_analysis%208489e112db2b433b90fed7d37fd18460/Untitled%202.png)

쿼리를 수행하면 orders 테이블과 order_payments 테이블을 조인해서 매출이 발생한 시점과 매출액 정보를 가져옵니다. 그런데 우리는 매출액이 발생한 일자만 필요합니다. DATE 함수를 이용해서 order_purchase_timestamp 값에서 일자만 추출해보겠습니다.

```sql
SELECT
	DATE(orders.order_purchase_timestamp) AS dt,
	order_payments.payment_value
FROM
	orders
LEFT JOIN order_payments
ON order_payments.order_id=orders.order_id
WHERE
	orders.order_purchase_timestamp >= "2017-01-01"
    AND orders.order_purchase_timestamp <= "2017-01-31"
```

![Untitled](ch4_13_sales_analysis%208489e112db2b433b90fed7d37fd18460/Untitled%203.png)

이제 일자별로 GROUP BY를 해주고, SUM을 해주면 각 일자별 매출을 집계할 수 있습니다. 그리고 결과를 보기 좋게 ORDER BY까지 적용해주면 됩니다.

```sql
SELECT
	DATE(orders.order_purchase_timestamp) AS dt,
	SUM(order_payments.payment_value) AS daily_sales
FROM
	orders
LEFT JOIN order_payments
ON order_payments.order_id=orders.order_id
WHERE
	orders.order_purchase_timestamp >= "2017-01-01"
    AND orders.order_purchase_timestamp <= "2017-01-31"
GROUP BY dt
ORDER BY dt
```

![Untitled](ch4_13_sales_analysis%208489e112db2b433b90fed7d37fd18460/Untitled%204.png)

한눈에 보기에도 일별 매출이 증가하는 추세를 볼 수 있었습니다. 이를 더 직관적으로 표현하려면 파이썬에서 위 SQL문을 실행시켜서 데이터를 가져오고, matplotlib으로 시각화 해주면 됩니다.

```sql
from matplotlib import pyplot as plt

with conn.cursor() as cursor:
    cursor.execute(daily_sales_sql)
    result = cursor.fetchall()

x_dates = []
y_sales = []
for date, sales in result:
    x_dates.append(date)
    y_sales.append(sales)
plt.plot(x_dates, y_sales)
plt.xticks(rotation=45, ha='right')
```

![Untitled](ch4_13_sales_analysis%208489e112db2b433b90fed7d37fd18460/Untitled%205.png)

### 연습문제

1. 2017년 주간 매출액 추이를 집계해보세요. YEARWEEK를 사용하면 편하게 집계할 수 있습니다. 비슷한 방식으로 월간 매출액 추이도 집계해보세요.