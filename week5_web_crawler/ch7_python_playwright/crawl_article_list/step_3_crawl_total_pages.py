import time

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


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
        last_page = page_list.find_all("a")[-1].get("data-id")
    return last_page


def crawl_total_page(playwright_page, date):
    page = 1
    while True:
        if page > 50:
            break
        html = crawl_single_article_html(playwright_page, date, page)
        last_page = parse_page_section(html)
        if last_page == "next":
            page += 10
            continue
        return last_page


if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        playwright_page = browser.new_page()
        date = "20240617"
        total_page = crawl_total_page(playwright_page, date)
        print("Total pages: ", total_page)
