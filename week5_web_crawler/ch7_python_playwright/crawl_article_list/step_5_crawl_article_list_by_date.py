import csv
import time

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from tqdm import tqdm


def crawl_single_article_html(playwright_page, date, page):
    url = f"https://sports.naver.com/kbaseball/news/index.nhn?isphoto=N&date={date}&page={page}"
    playwright_page.goto(url, wait_until="load", timeout=30000)
    time.sleep(1)
    html = playwright_page.content()
    return html


def parse_article_list(html, date):
    soup = BeautifulSoup(html, "lxml")
    news_items = soup.find("div", id="_newsList").find("ul").find_all("li")
    data = []
    for item in news_items:
        url = item.find("a").get("href")
        title = item.find("a", class_="title").text.strip()
        data.append({
            "date": date,
            "title": title,
            "url": url,
        })
    return data


def parse_page_section(html):
    soup = BeautifulSoup(html, "lxml")
    page_list = soup.find("div", id="_pageList")
    next_button = page_list.find("a", class_="next")
    if next_button:
        last_page = "next"
    else:
        last_page = int(page_list.find_all("a")[-1].get("data-id"))
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


def crawl_article_list_by_date(playwright_page, date):
    total_data = []
    total_page = crawl_total_page(playwright_page, date)
    print(f"total pages: {total_page} start crawling!")
    for i in tqdm(range(total_page)):
        html = crawl_single_article_html(playwright_page, date, i + 1)
        data = parse_article_list(html, date)
        total_data.extend(data)
    print(f"Completed crawling {len(total_data)} articles.")
    return total_data


def write_article_list(data):
    with open("./data/total_article_list.csv", "w") as fw:
        writer = csv.DictWriter(fw, fieldnames=["date", "url", "title"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        playwright_page = browser.new_page()
        date ="20240617"
        data = crawl_article_list_by_date(playwright_page, date)
    write_article_list(data)
