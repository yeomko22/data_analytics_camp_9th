import time

from bs4 import BeautifulSoup


def crawl_single_article_html(playwright_page, date, page):
    url = f"https://sports.naver.com/kbaseball/news/index.nhn?isphoto=N&date={date}&page={page}"
    playwright_page.goto(url, wait_until="load", timeout=30000)
    time.sleep(1)
    html = playwright_page.content()
    return html


def parse_page_section(html):
    soup = BeautifulSoup(html, "lxml")
    page_list = soup.find("div", id="_pageList")
    next_button = page_list.find("a", class_="next")
    if next_button:
        last_page = "next"
    else:
        page_list_str = page_list.text.strip()
        last_page = page_list_str.split("\n")[-1]
        last_page = int(last_page)
    return last_page


if __name__ == '__main__':
    with open("./data/article_list_first.html") as fr:
        article_list_html = fr.read()
        last_page = parse_page_section(article_list_html)
        print(last_page)

    with open("./data/article_list_last.html") as fr:
        article_list_html = fr.read()
        last_page = parse_page_section(article_list_html)
        print(last_page)
