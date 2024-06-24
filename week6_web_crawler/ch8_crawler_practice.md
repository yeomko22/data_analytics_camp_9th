# ch8_crawler_practice

## Playwright 이용해서 크롤러 짜기

크롤링을 익혀보기 위해서 연습을 한번 해보겠습니다. 네이버에 특정 검색어를 입력하여 뉴스 10 페이지를 수집하는 크롤러를 짜보겠습니다. 먼저 특정 검색어를 입력했을 때, 뉴스 제목 위에 네이버뉴스라고 뜨는 링크의 URL을 수집합니다.

![Untitled](ch8_crawler_practice/Untitled.png)

그 다음, 뉴스 상세 페이지로 이동하여 뉴스의 제목과 본문을 수집하면 됩니다.

![Untitled](ch8_crawler_practice/Untitled%201.png)

수집한 결과는 CSV 파일에 기록하면 됩니다.
