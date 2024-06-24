import csv
import time

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from tqdm import tqdm
from datetime import datetime, timedelta


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
    article_content = soup.find("div", class_="_article_content")
    video_area = article_content.find("div", class_="video_area")
    if video_area:
        video_area.decompose()
    content = article_content.text.strip()
    article_dict = {
        "date": date,
        "url": url,
        "title": title,
        "content": content
    }
    return article_dict


def write_article_dict_list(article_dict_list):
    with open(f"./data/article/{date}.csv", "w") as fw:
        writer = csv.DictWriter(fw, fieldnames=["date", "url", "title", "content"])
        writer.writeheader()
        for row in article_dict_list:
            writer.writerow(row)


def generate_datelist():
    start_date = datetime(2023, 12, 20)
    end_date = datetime(2024, 1, 1)
    datelist = []
    while start_date < end_date:
        datelist.append(start_date.strftime("%Y%m%d"))
        start_date += timedelta(days=1)
    return datelist


def crawl_article_by_date(article_list):
    parsed_article_list = []
    with open("./data/failed.csv", "a") as fw:
        writer = csv.writer(fw)
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            playwright_page = browser.new_page()
            for article_list_dict in tqdm(article_list):
                retry = 2
                is_success = False
                while retry:
                    url = article_list_dict["url"]
                    date = article_list_dict["date"]
                    try:
                        article_html = crawl_article_html(playwright_page, url)
                        parsed_article_dict = parse_article(date, url, article_html)
                        parsed_article_list.append(parsed_article_dict)
                        is_success = True
                        break
                    except Exception as e:
                        # print(f"RETRY crawl page {url}.", e)
                        retry -= 1
                        continue
                if not is_success:
                    print(f"Failed to crawl page {url}")
                    writer.writerow([url])
    return parsed_article_list


def load_article_list(date):
    article_list = []
    with open(f"./data/article_list/{date}.csv") as fr:
        reader = csv.DictReader(fr)
        for row in reader:
            article_list.append(row)
    return article_list


def run(date):
    print(f"start crawl {date}")
    article_list = load_article_list(date)
    parsed_article_list = crawl_article_by_date(article_list)
    write_article_dict_list(parsed_article_list)


if __name__ == '__main__':
    datelist = generate_datelist()
    for i, date in enumerate(datelist):
        run(date)
