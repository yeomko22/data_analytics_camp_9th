import csv

from bs4 import BeautifulSoup


def parse_article_list(html):
    soup = BeautifulSoup(html, "lxml")
    news_items = soup.find("div", id="_newsList").find("ul").find_all("li")
    data = []
    for item in news_items:
        url = item.find("a").get("href")
        title = item.find("a", class_="title").text.strip()
        data.append({
            "url": url,
            "title": title
        })
    return data


if __name__ == '__main__':
    with open("./data/article_list_first.html") as fr:
        article_list_html = fr.read()
    data = parse_article_list(article_list_html)
    print(data)
