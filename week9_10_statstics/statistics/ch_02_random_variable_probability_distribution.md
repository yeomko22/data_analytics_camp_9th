# ch2. 확률 변수와 확률 분포

표본 공간(Sample Space): 시행의 결과로 나올 수 있는 모든 결과의 집합. 

ex) 동전 두개를 던져서 나올 수 있는 앞면, 뒷면 조합

확률 변수(Random Variable): 표본 공간의 각 사건에 실수 값을 부여하는 함수. 

ex) 동전 두개를 던져서 나온 앞면의 개수, 0, 1, 2

확률 분포(Probability Distribution): 확률 변수가 취할 수 있는 모든 값과 그 값들이 나타날 확률을 매핑한 함수

ex) 앞면이 0개일 확률: 1/4, 앞면이 1개 나올 확률 2/4, 앞면이 2개 나올 확률 1/4

![Untitled](./images/Untitled.png)

이산형 확률 변수(Discrete Random Variable): 확률 변수 X의 집합이 셀 수 있으면 이산 확률 변수

ex) 동전 2개를 던져서 나올 수 있는 앞면의 개수

연속형 확률 변수(Continuous Random Variable): 확률 변수 X의 집합이 셀 수 없으면 연속 확률 변수

ex) 남학생들의 키

## 이산 확률 분포

확률 분포란 확률 변수와 확률 값을 매핑한 함수! 이산 확률 변수는 개수가 정해져 있기 때문에 확률분포표로 그릴 수 있다. 동전 2개를 던져서 나온 앞면의 개수의 확률 분포표를 그려보자.

| X | 0 | 1 | 2 |
| --- | --- | --- | --- |
| P(X) | 1/4 | 2/4 | 1/4 |

| X | X1 | X2 | … | X3 |
| --- | --- | --- | --- | --- |
| P(X) | P1 | P2 | … | P |
1. 각 확률값들은 0이상 1이하이다.
2. 모든 사건들에 대한 확률값을 모두 더하면 1이 된다.
3. 모든 사건은 서로 배반 사건이다. (즉, 주사위를 하나 던졌는데 1인 동시에 2가 나올 수 없다.)

## 연속 확률 분포

연속 확률 변수에 대한 확률 분포를 말한다. 예를들어 고등학교 남학생 1000명을 뽑았고, 이들의 키는 160에서 190cm 사이라고 가정한다. 확률 분포를 구하기 위해서 이를 구간으로 나누고, 확률을 계산할 수 있다. 이를 도수 분포표라고 부릅니다.

| 확률 변수 구간 | 도수 | 상대 도수 | 상대 도수 / 계급의 크기 |
| --- | --- | --- | --- |
| 160 ~ 170 | a | a/1000 | a / 10000 |
| 170 ~ 180 | b | b/1000 | b / 10000 |
| 180 ~ 190 | c | c/1000 | c / 10000 |

그러면 특정 계급에 속하는 학생 수는 계급의 크기 * (상대 도수 / 계급의 크기)로 나타낼 수 있습니다. 이 성질을 이용해서 히스토그램을 그려보겠습니다.

![Untitled](./images/Untitled%201.png)

이 때, 확률 변수 구간을 점점 더 잘게 잘게 쪼개면 우리가 잘 알고 있는 종모양의 분포에 가까워집니다.

![Untitled](./images/Untitled%202.png)

이제 각 히스토그램의 중간점들을 이어주면 곡선이 나옵니다. 이를 확률 밀도 함수의 그래프라고 부르고, 영어로는 pdf(probaility density function)이라고 부른다. 

연속 확률 분포에서는 구간에 대한 확률값을 구합니다. 특정 지점에 대해서 확률을 구할 경우에는 확률 값이 0이 됩니다.

ex) 구간 확률 P(170 ≤ X ≤ 180), 지점 확률 P(X=170)

구간의 확률값은 구간 안의 막대들의 넓이의 합입니다. 이는 곧 확률 밀도 함수의 구간 적분값이 됩니다.

## 정규 분포

정규 분포는 연속 확률 분포의 한 종류이자, 아주아주 중요한 분포입니다. 먼저 확률 밀도 함수 식을 보겠습니다. 

$$
f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2} (-\infty<x<\infty)
$$

식 자체는 무시무시하지만, 이를 암기할 필요는 전혀 없습니다. 기억해야할 것은 정규 분포의 형태는 평균과 표준편차, 두 가지 변수에 의해서 결정된다는 점만 기억하면 됩니다.

![Untitled](./images/Untitled%203.png)

정규분포는 평균값을 중심으로 좌우 대칭의 형태를 갖게 됩니다. 그리고 표준 편차가 클 수록 퍼지게 되고, 작을 수록 뾰족해집니다.

어떤 연속 확률 변수가 정규 분포를 따른다는 것은 아래처럼 표기할 수 있습니다.

$$
X\sim N(\mu, \sigma^2)
$$

## 표준 정규 분포

평균이 0이고 표준편차가 1인 정규분포를 말합니다. 아래 그래프에서 빨간색으로 표시된 분포가 표준 정규 분포입니다. 표준 정규분포가 왜 중요하나면, 표준 정규 분포에 대해서 미리 구간별 확률값을 계산했기 때문입니다.

![Untitled](./images/Untitled%203.png)

연속 확률 변수의 확률 분포에서 확률값은 특정 구간의 면적이라고 했습니다. 그런데 엄청나게 복잡하게 생긴 정규 분포 식을 구간별로 적분하는 것은 보통 일이 아닙니다. 모든 평균과 표준 편차에 대해서 이 계산을 일일이 할 수 없기 때문에, 표준 정규 분포에 대해서 미리 구간별 적분을 해놓고, 이를 이용해서 다양한 분포들에 대해 확률을 계산하는 것입니다.

정규분포 확률 계산: [https://homepage.divms.uiowa.edu/~mbognar/applets/normal.html](https://homepage.divms.uiowa.edu/~mbognar/applets/normal.html)

![Untitled](./images/Untitled%204.png)