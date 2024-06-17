# ch10_playwright

## Browser를 이용한 크롤링

지금까지 우리는 개발자 도구를 이용하여 직접 서버와 클라이언트가 주고 받는 데이터를 확인하고, 직접 HTTP request 날려서 데이터를 받아오는 방식으로 크롤링을 했습니다. 하지만 python playwright 라이브러리를 사용하면 마치 우리가 브라우저를 통해서 웹 서핑을 하는 방식으로 크롤링을 할 수 있습니다.

### 설치

pip을 이용해서 playwright 라이브러리를 먼저 설치합니다.

```python
pip install playwright 
```

## Playwright 기본 사용법

미리 다운로드 받은 크롬 드라이버 경로를 전달하여 드라이버를 생성합니다.

```python
from selenium import webdriver

driver = webdriver.Chrome("./driver/chromedriver")
```

driver.get 함수를 이용하면 특정 URL로 이동할 수 있습니다.

```python
url = "https://sports.news.naver.com/kbaseball/news/index?isphoto=N"
driver.get(url)
```

driver.find_element 함수를 이용하면 현재 화면에서 HTML 요소들을 찾을 수 있습니다. 이때, By를 사용하게 되는데 By.CLASS_NAME, By.ID, By.TAG_NAME 등을 사용하여 웹 페이지 구성 요소들을 찾을 수 있습니다.

```python
from selenium.webdriver.common.by import By

news_list = driver.find_element(By.CLASS_NAME, "news_list")
news_titles = [news_item.find_element(By.CLASS_NAME, "title") for news_item in news_items]
news_items = news_list.find_elements(By.TAG_NAME, "li")

```

찾아낸 element에 get_property 함수를 사용하면 속성 값들을 파싱할 수 있습니다.

```python
news_urls = [news_title.get_property("href") for news_title in news_titles]
```

이를 이용해서 브라우저를 이용해서 URL들을 이동하면서 원하는 데이터를 크롤링하면 됩니다.

### 장점

직관적이고 간단하게 데이터를 크롤링 할 수 있습니다. 또한 서버 API를 직접 찔러서 받아오기 까다로운 데이터들을 받아오기가 쉽고, 네이버 이미지 검색 결과 처럼 javascript 데이터 안에 들어있다가 화면에 렌더링 되는 데이터들을 수집하는 것이 쉽습니다.

또한 playwright 장점은 매크로를 만들 수 있다는 점 입니다. 예를들어 기차표를 예매하는 playwright 프로그램을 만들거나, 아이돌 콘서트 예매하는 매크로를 만들 수 있습니다.

### 한계

playwright 브라우저로 특정 URL에 접속합니다. 때문에 우리가 원하지 않더라도 화면을 렌더링하는데 필요한 모든 요청과 리소스들을 받아오게 됩니다. 필연적으로 속도가 느립니다. 수십만개의 페이지를 요청해야하는 상황에는 적합하지 않습니다.