# ch7_distinct_group_by_sum_count

## DISTINCT 문의 사용

SELECT 문과 함께 DISTINCT를 사용하면 특정 컬럼의 유니크한 값들만 가져올 수 있습니다.

```sql
SELECT DISTINCT "컬럼명"
FROM "테이블 명";
```

타이타닉 테이블에서 Pclass가 어떤 것들이 있는지 조회해보겠습니다.

```sql
SELECT DISTINCT Pclass
FROM titanic;
```

![Untitled](ch4_7_distinct_group_by_sum_count%2097f3571eb52044689f13e4dad38636e0/Untitled.png)

승선지가 어떤 곳들이 있는지 조회해 보겠습니다.

```sql
SELECT DISTINCT Embarked
FROM titanic;
```

![Untitled](ch4_7_distinct_group_by_sum_count%2097f3571eb52044689f13e4dad38636e0/Untitled%201.png)

이처럼 DISTINCT는 안에 어떤 값들이 들어있는지 잘 모르는 데이터 셋을 처음 받았을 때, 특정 컬럼에 어떤 값들이 들어있는지 확인하기 위해서 많이 사용합니다.

## COUNT

컬럼들의 개수를 셀 때 COUNT를 사용합니다. 뒤에 따라붙는 AS는 SQL 실행 결과로 가져오는 데이터의 컬럼명을 지정하는 것입니다. 아래 예시에서 AS로 지정하지 않으면 결과 컬럼명이 COUNT(*)로 그대로 나옵니다.

```sql
SELECT COUNT(*) AS cnt
FROM "테이블 명"
WHERE "조건"
```

COUNT를 이용해서 titanic 테이블의 전체 레코드 개수를 집계해보겠습니다.

```sql
SELECT COUNT(*) AS cnt
FROM titanic;
```

titanic 테이블에서 생존자 수만 집계해보겠습니다.

```sql
SELECT COUNT(*) as cnt
FROM titanic
WHERE Survived=1;
```

![Untitled](ch7_distinct_group_by_sum_count/Untitled%202.png)

이번에는 생존했고, 1등칸에 탔던 사람들만 집계해보겠습니다.

```sql
SELECT COUNT(*) as cnt
FROM titanic
WHERE 
	Survived=1
	AND Pclass=1;
```

![Untitled](ch7_distinct_group_by_sum_count/Untitled%203.png)

### 연습 문제

1. 운임을 10달러 보다 적게 낸 승객의 수를 집계하세요.
2. 운임을 10달러 보다 적게 낸 승객 중 생존자 수를 집계하세요.

## Sum, Avg

COUNT와 비슷하게 특정 컬럼의 값들을 모두 더하거나, 평균을 구하는 작업도 SQL문으로 가능합니다.

전체 승객의 운임의 합을 구해보겠습니다.

```sql
SELECT SUM(Fare) as sum_fare
FROM titanic;
```

![Untitled](ch7_distinct_group_by_sum_count/Untitled%204.png)

전체 승객의 평균 연령을 한번 구해보겠습니다.

```sql
SELECT AVG(Age) as avg_age
FROM titanic
```

![Untitled](ch7_distinct_group_by_sum_count/Untitled%205.png)

마찬가지로 WHERE 문으로 조건을 걸어서 집계를 할 수도 있습니다. 생존자들 가운데 1등석에 탄 승객들의 평균 연령을 구해보겠습니다. 

```sql
SELECT AVG(Age) as avg_age
FROM titanic
WHERE
	Survived=1
	AND Pclass=1;
```

![Untitled](ch7_distinct_group_by_sum_count/Untitled%206.png)

### 연습문제

1. 1등석, 2등석, 3등석 승객들의 총 운임, 평균 운임을 각각 구하세요.
2. 형제자매, 배우자가 동승한 승객들의 수를 집계하세요. 
3. 형제자매, 배우자가 동승한 승객들의 평균 운임을 집계하세요.

### Group by

Sum과 Avg문으로 집계를 수행하다 보면 불편한 점이 발생합니다. 1등석, 2등석, 3등석 별로 따로따로 SQL문을 돌려야 하는데, 이를 그냥 특정 컬럼을 기준으로 그룹을 묶고, 그룹별로 계산을 하면 안될까요? 이럴 때 GROUP BY를 사용하면 됩니다.

```sql
SELECT "그룹명", "집계 쿼리 ex) SUM, AVG 등"
FROM "테이블명"
GROUP BY "그룹명"
```

GROUP BY를 사용할 때는 SELECT 문에서 해당 그룹별로 묶은 레코드 들에 대해서 집계 쿼리를 날려주어야합니다. 그리고 그룹으로 묶어준 컬럼을 함께 읽어와야 결과를 해석하기에 편리합니다.

한번 좌석 등급별로 평균 연령을 집계해보겠습니다.

```sql
SELECT Pclass, AVG(Age) as avg_age
FROM titanic
GROUP BY Pclass;
```

![Untitled](ch7_distinct_group_by_sum_count/Untitled%207.png)

점점 뭔가 분석 다운 분석을 하고 있는거 같죠? 

그룹을 여러개를 지정할 수도 있습니다.

```sql
SELECT "그룹명 1", "그룹명 2", "집계 쿼리 ex) SUM, AVG 등"
FROM "테이블명"
GROUP BY "그룹명 1", "그룹명 2"
```

좌석 등급과 생존 여부에 따른 평균 연령을 집계해보겠습니다. 이 경우 총 6개의 그룹이 나오게 됩니다. (좌석 등급 개수 * 생존 여부)

```sql
SELECT Pclass, Survived, AVG(Age) as avg_age
FROM titanic
GROUP BY Pclass, Survived;
```

![Untitled](ch7_distinct_group_by_sum_count/Untitled%208.png)

간단한 SQL문 한번으로 좌석 등급이 낮을 수록 평균 연령이 낮고, 사망자는 생존자보다 평균 연령이 높다는 인사이트를 뽑아낼 수 있었습니다.

### 연습 문제

1. 좌석 등급, 성별로 그룹을 지어 평균 연령을 집계해보세요.
2. 승선지, 좌석 등급으로 그룹을 지어 몇명의 승객이 탔는지 집계해보세요.

## Having의 사용

having은 그룹마다 조건을 주고 싶을 때 사용합니다. WHERE와 비슷하다고 생각이 들 수 있겠지만, HAVING은 조건을 걸어서 그룹을 걸러낼 때 사용합니다.

```sql
SELECT "그룹명 1", "그룹명 2", "집계 쿼리 ex) SUM, AVG 등"
FROM "테이블명"
GROUP BY "그룹명 1", "그룹명 2"
HAVING "조건명"
```

예를들어 보겠습니다. 승선지 별로 평균 연령을 한번 집계해보겠습니다.

```sql
SELECT Embarked, AVG(Age) as avg_age
FROM titanic
WHERE Embarked != ""
GROUP BY Embarked;
```

![Untitled](ch7_distinct_group_by_sum_count/Untitled%209.png)

그런데 승선지 별로 탑승객 수를 집계해보면 Q에서 탄 사람의 수가 다른 승선지에 비해서 작습니다.

```sql
SELECT Embarked, COUNT(*) as cnt
FROM titanic
WHERE Embarked != ""
GROUP BY Embarked;
```

![Untitled](ch7_distinct_group_by_sum_count/Untitled%2010.png)

HAVING을 이용해서 탑승객의 수가 50명 이상인 승선지들에 한하여 평균 연령을 집계해보겠습니다.

```sql
SELECT Embarked, AVG(Age) as avg_age
FROM titanic
WHERE Embarked != ""
GROUP BY Embarked;
HAVING COUNT(*) >= 50;
```

![Untitled](ch7_distinct_group_by_sum_count/Untitled%2011.png)

HAVING문은 그룹이 너무 많을 때, 특정 조건을 충족하는 그룹들만 걸러내서 데이터를 집계하고 싶을 때 사용합니다. 엄청 자주 사용되는 문법은 아닙니다.

## 정리

이번 챕터에서는 SUM, COUNT, AVG와 같은 연산자를 배웠습니다. 그리고 GROUP BY와 함께 사용해서 각종 데이터 집계 작업을 수행해보았습니다. python 코드로 짰을 때는 if와 for문을 사용해서 복잡하게 코드를 짰던 것과 비교해보면 매우 간결하고 편리하게 데이터를 집계할 수 있었습니다. 이와 같이 SQL을 활용해서 데이터를 분석하는 작업은 데이터 분석가의 기본 소양이니, 잘 익히고 넘어가길 바랍니다.