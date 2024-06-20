import time

from bs4 import BeautifulSoup


def parse_article(html):
    soup = BeautifulSoup(html, "lxml")
    title = soup.find("h2").text
    article_content = soup.find("div", class_="_article_content")
    video_area = article_content.find("div", class_="video_area")
    if video_area:
        video_area.decompose()
    content = article_content.text.strip()
    return {
        "title": title,
        "content": content
    }


if __name__ == '__main__':
    with open("./data/article_video.html") as fr:
        article_html = fr.read()
        data = parse_article(article_html)
        print(data)

# SELECT
#     DATE_FORMAT(trans_date, "%Y-%m") as month,
#     country,
#     COUNT(*) as trans_count,
#     COUNT(IF(state="approved", 1, NULL)) as approved_count,
#     SUM(amount) AS trans_total_amount,
#     SUM(IF(state="approved", amount, 0)) as approved_total_amount
# FROM
#     Transactions
# GROUP BY
#     month,
#     country
