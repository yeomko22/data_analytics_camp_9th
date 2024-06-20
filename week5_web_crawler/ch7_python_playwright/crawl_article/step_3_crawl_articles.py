import csv
import time

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from tqdm import tqdm


def crawl_article_html(playwright_page, url):
    playwright_page.goto(url, wait_until="load", timeout=30000)
    time.sleep(0.5)
    html = playwright_page.content()
    return html


def load_data():
    total_data = []
    with open("./data/total_article_list.csv") as fr:
        reader = csv.DictReader(fr)
        for row in reader:
            total_data.append(row)
    return total_data


def parse_article(date, url, html):
    soup = BeautifulSoup(html, "lxml")
    title = soup.find("h2").text
    content = soup.find("div", class_="_article_content").text
    article_dict = {
        "date": date,
        "url": url,
        "title": title,
        "content": content
    }
    return article_dict


def write_article_dict_list(article_dict_list):
    with open(f"./data/{date}.csv", "w") as fw:
        writer = csv.DictWriter(fw, fieldnames=["date", "url", "title", "content"])
        writer.writeheader()
        for row in article_dict_list:
            writer.writerow(row)


if __name__ == '__main__':
    data = load_data()
    article_dict_list = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        playwright_page = browser.new_page()
        for i, row in tqdm(enumerate(data), total=len(data)):
            retry = 2
            is_success = False
            while retry:
                try:
                    date = row["date"]
                    url = row["url"]
                    html = crawl_article_html(playwright_page, url)
                    article_dict = parse_article(date, url, html)
                    article_dict_list.append(article_dict)
                    is_success = True
                    break
                except Exception as e:
                    print(f"RETRY CRAWL: {url}")
                    retry -= 1
                    continue
            if not is_success:
                print(f"Failed to crawl {url} after retrying.")
    write_article_dict_list(article_dict_list)
