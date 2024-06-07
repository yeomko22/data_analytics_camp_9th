# ch8_case_if

## 교재

6장을 보시면 됩니다.

## IF 문의 사용

SQL문을 사용하다가 SELECT 시에 IF문을 사용하고 싶을 수 있습니다. 그럴 때 IF 문으로 조건을 달 수 있습니다. 이를 사용하면 굳이 update를 하지 않더라도 조건에 따라 값을 변형해서 읽을 수 있습니다.

```sql
SELECT
	IF ("조건", "조건이 True일때 리턴하는 값", "조건이 False일 때 리턴하는 값")
FROM
	"테이블 명"
```

예를 들어서 타이타닉 승객들의 연령이 10세 이하면 child, 그 이상은 adult라고 리턴하도록 읽어보겠습니다.

```sql
SELECT
	PassengerId,
   Age,
	IF (Age <= 10, "child", "adult") AS ischild
FROM
	titanic;
```

![Untitled](ch4_8_case_if%20614140a321b1497daeaefb90a30498ea/Untitled.png)

### 연습 문제

1. 운임을 50달러 이하로 지불한 승객은 NORMAL, 그보다 많이 지불한 승객은 VIP로 읽어보세요.

## Case 문의 사용

그런데 조건을 여러개 넣고 싶을 때는 어떻게 할까요?  python에서라면 elif를 썼겠지만, SQL문에서는 CASE를 쓰면 됩니다.

```sql
SELECT
	CASE
		WHEN "조건 1" THEN "조건 1이 True일 때 값"
		WHEN "조건 2" THEN "조건 2가 True일 때 값"
		...
		ELSE "위에 조건들이 모두 만족되지 않았을 때 갖는 값"
	END AS "컬럼 닉네임"
FROM "테이블 명"
```

타이타닉 테이블에서 10세 이하 승객은 child, 11세부터 20세 이하 승객은 teenager, 그 이상은 adult로 읽어보겠습니다.

```sql
SELECT
	PassengerId,
  Age,
	CASE
		WHEN Age <= 10 THEN "child"
		WHEN Age <= 20 THEN "teenager"
		ELSE "adult"
	END AS age_interval
FROM
	titanic;
```

## 집계 쿼리와 Case문 사용

집계를 할 때, 조건을 집어넣고 싶다면 Case문을 활용하면 됩니다. 

```sql
SELECT 
	SUM(CASE WHEN "조건" THEN 1 END) AS "컬럼 닉네임"
FROM "테이블 명"
```

좌석 등급별 생존율를 집계해보겠습니다. 

```sql
SELECT
	COUNT(CASE WHEN Survived=1 THEN 1 END) / COUNT(*)
FROM titanic
GROUP BY Pclass
```

![Untitled](ch8_case_if/Untitled%201.png)

좌석 등급과 성별에 따른 생존율을 집계해보겠습니다.

```sql
SELECT
	Pclass,
    Sex,
	COUNT(CASE WHEN Survived=1 THEN 1 END) / COUNT(*) AS survived_ratio
FROM titanic
GROUP BY Pclass, Sex
```

![Untitled](ch8_case_if/Untitled%202.png)

### 연습문제
1. https://leetcode.com/problems/capital-gainloss

## 정리

이번 장에서는 IF문과 CASE문을 사용해서 SELECT 문에 조건문을 집어넣는 연습을 해보았습니다. 실제로도 자주 사용하는 문법이니, 잘 기억해주세요.
