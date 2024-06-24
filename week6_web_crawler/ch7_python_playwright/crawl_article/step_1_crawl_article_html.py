import time

from playwright.sync_api import sync_playwright


def crawl_article_html(playwright_page, url):
    playwright_page.goto(url, wait_until="load", timeout=30000)
    time.sleep(1)
    html = playwright_page.content()
    return html


if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        playwright_page = browser.new_page()
        # url = "https://m.sports.naver.com/kbaseball/article/477/0000496335"
        url = "https://m.sports.naver.com/kbaseball/article/056/0011742265"
        html = crawl_article_html(playwright_page, url)
        with open("./data/article_video.html", "w") as fw:
            fw.write(html)
