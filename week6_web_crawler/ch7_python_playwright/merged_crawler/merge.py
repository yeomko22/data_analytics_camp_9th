from datetime import datetime, timedelta
from tqdm import tqdm
import csv


def generate_datelist():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 1, 1)
    datelist = []
    while start_date < end_date:
        datelist.append(start_date.strftime("%Y%m%d"))
        start_date += timedelta(days=1)
    return datelist


def merge(datelist):
    with open("./data/merged.csv", "w") as fw:
        writer = csv.DictWriter(fw, fieldnames=["date", "url", "title", "content"])
        writer.writeheader()
        for date in tqdm(datelist):
            with open(f"./data/article/{date}.csv") as fr:
                reader = csv.DictReader(fr)
                for row in reader:
                    writer.writerow(row)


if __name__ == '__main__':
    datelist = generate_datelist()
    merge(datelist)

