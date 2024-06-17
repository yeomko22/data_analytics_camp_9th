# ch6_analyze_web_service

## Postman 사용하기

시작하기에 앞서서 HTTP 요청을 쉽게 조작할 수 있는 Postman이라는 프로그램을 설치하시기 바랍니다. 브라우저를 이용하면 HTTP GET 요청밖에 보낼 수 없고, 요청에 실어보내는 파라미터를 수정하기가 어렵습니다. postman을 이용하면 HTTP 요청과 관련된 거의 대부분의 기능들을 편하게 사용할 수 있습니다.

[https://www.postman.com/](https://www.postman.com/)

![Untitled](ch6_analyze_web_service/Untitled.png)

## 웹 사이트 구조 파악

크롤링에 앞서서 내가 데이터를 수집하고자 하는 웹 사이트가 어떻게 동작하는지 파악해야합니다. 내가 원하는 데이터를 수집하기 위해서 웹 페이지를 그대로 수집하면 되는지, 아니면 백엔드 API를 찔러서 데이터를 받아와야 하는지를 결정해야 합니다.

### 크롤링 대상 선정

먼저 수집하고자 하는 데이터를 선정해야합니다. 여기서는 한국 프로 야구와 관련된 국내 기사를 수집해보겠습니다. 네이버 스포츠는 국내 주요 스포츠 미디어들의 기사들을 한 곳에서 모아 볼 수 있는 서비스를 제공하고 있었습니다. 따라서 네이버 스포츠 서비스를 크롤링해서 2022년 한 해 동안의 한국 야구 뉴스 기사들을 수집해보겠습니다.

![Untitled](ch6_analyze_web_service/Untitled%201.png)

### URL 구조 파악하기

HTTP GET 요청은 기본 URL 뒤에 ?를 붙인 뒤, 파라미터를 붙여서 요청을 보냅니다. 네이버 스포츠의 경우 아래와 같은 포맷으로 요청을 보내면, 특정일의 특정 페이지 뉴스 기사들을 가져올 수 있습니다.

```python
https://sports.news.naver.com/kbaseball/news/index?isphoto=N&date={"날짜"}&page={"페이지 번호"}
```

```python
# 예시: 2023년 5월 10일 페이지 3
https://sports.news.naver.com/kbaseball/news/index?isphoto=N&date=20230510&page=3
```

![Untitled](ch6_analyze_web_service/Untitled%202.png)

### 수집하고자 하는 데이터가 들어있는 HTML 태그 확인하기

이제 개발자 도구를 이용하여 수집하고자 하는 데이터가 어느 HTML 태그에 들어있는지 확인해봅니다. 여기서는 특정 요일의 야구 기사들의 링크를 수집하고자 합니다. 크롬 개발자 도구를 이용하여 확인해보니, <div class=news_list> 안에 <ul> 태그 안에 <li> 태그 안에 들어있습니다.

![Untitled](ch6_analyze_web_service/Untitled%203.png)

### HTTP 요청을 보내어 원하는 데이터가 들어있는지 확인해보기

Postman으로 해당 URL로 요청을 보내어 데이터가 들어있는지 확인해보겠습니다.

![Untitled](ch6_analyze_web_service/Untitled%204.png)

확인해본 결과, <div class=”news_list”>가 비어있습니다. 이는 해당 웹 페이지가 프론트엔드 요소들이 먼저 뜬 후, 백엔드에 데이터를 요청해서 받아와서 렌더링하는 클라이언트 사이드 렌더링 방식으로 동작하기 때문입니다. 다시 개발자 도구를 열어서 백엔드로부터 어떤 데이터를 받아오는지 확인해보겠습니다.

### 개발자 도구를 사용해서 백엔드로부터 전송받는 데이터 확인

개발자 도구를 열어서 Network 탭을 선택한 다음, 새로고침을 눌러보겠습니다. 

![Untitled](ch6_analyze_web_service/Untitled%205.png)

그러면 list?page=3…와 같은 URL과 함께 Response에 json 포맷으로 데이터가 전송된 것을 확인할 수 있습니다. (json이란 python 딕셔너리와 비슷하게 key와 value로 이루어진 데이터 포맷입니다.) 이 요청의 URL만 복사해서 Postman으로 요청을 날려보겠습니다.

![Untitled](ch6_analyze_web_service/Untitled%206.png)

자, 우리가 그토록 찾아헤메던 특정 요일, 특정 페이지의 뉴스 기사 목록을 가져올 수 있었습니다.

### 기사 페이지 분석

이제 각각의 뉴스 기사 페이지를 분석해보겠습니다. 뉴스 기사 페이지 URL은 oid, aid 두개의 파라미터를 통해 요청을 할 수 있었습니다. 그리고 이 데이터는 방금 우리가 수집한 json 데이터 안에 들어있었습니다.

![Untitled](ch6_analyze_web_service/Untitled%207.png)

그러면 저 URL로 요청을 보내면 뉴스 원문 텍스트를 수집할 수 있는지 확인해보겠습니다.

![Untitled](ch6_analyze_web_service/Untitled%208.png)

다행히 텍스트가 잘 들어있네요. 이 부분은 서버에서 HTML에 잘 조립한 뒤, 내려주는 모양입니다.

## 크롤러 설계하기

기사 목록 페이지와 기사 페이지의 동작 방식을 알았으니, 크롤러를 설계할 수 있습니다.

1. 기사 목록을 내려주는 백엔드 API에 요청을 보내어 oid와 aid를 가져온다.
2. oid와 aid를 가지고 기사 URL을 만들어서 요청을 보낸 뒤, 응답 HTML을 파싱하여 기사의 제목과 본문 데이터를 수집한다.

## 정리

지금까지 데이터를 수집하기 위해 웹 사이트의 구조를 분석하는 일련의 과정을 소개하였습니다. 

1. 크롤링 대상을 선정
2. URL 구조를 분석
3. 실제 요청을 보내봐서 내가 얻고자 하는 데이터가 들어있는지 확인
4. 없을 경우 백엔드 서버와 어떤 요청을 주고 받는지 확인
5. 백엔드 API에 직접 요청을 보내어 데이터 수집

물론, 데이터를 수집하고자 하는 대상에 따라서 분석 방법은 달라질 수 있습니다. 상황에 따라서 적절하게, 내가 수집하고자 하는 데이터를 모으면 됩니다. 다음 장에서는 본격적으로 python을 이용해 크롤러를 개발해보겠습니다.