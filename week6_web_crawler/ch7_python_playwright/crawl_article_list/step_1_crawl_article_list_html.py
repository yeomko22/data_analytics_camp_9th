import time

from playwright.sync_api import sync_playwright


def crawl_article_list_html(playwright_page, date, page):
    url = f"https://sports.naver.com/kbaseball/news/index.nhn?isphoto=N&date={date}&page={page}"
    playwright_page.goto(url, wait_until="load", timeout=30000)
    time.sleep(1)
    html = playwright_page.content()
    return html


if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        playwright_page = browser.new_page()
        date = "20240617"
        page = 11
        html = crawl_article_list_html(playwright_page, date, page)
        with open("./data/article_list_last.html", "w") as fw:
            fw.write(html)
