import requests
import selectorlib
from lxml import html
from bs4 import BeautifulSoup
from datetime import datetime


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape_bmt(url):
    """Scrape the page source from the URL"""
    page = requests.get(url, headers=HEADERS)

    data = page.text
    print(data)

    file = open("scraped_bmt.txt", 'w')
    file.writelines(data)



def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract_bmt.yaml")
    value = extractor.extract(source)["show"]
    return value


def scrape_cb(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    extractor = selectorlib.Extractor.from_yaml_file("extract_cb.yaml")
    value = extractor.extract(source)["band"]
    print(value)


def scrape_central():
    response = requests.get("https://www.centralsaloon.com/events", headers=HEADERS)
    source = response.text
    extractor = selectorlib.Extractor.from_yaml_file("extract_central.yaml")
    band = extractor.extract(source)["band"][0]
    month = str(extractor.extract(source)["month"])
    day = extractor.extract(source)["day"]

    current_month = datetime.now().month
    if current_month == 12 and month == "Jan":
        year = "2025"
    else:
        year = datetime.now().year

    date = f"{month} {day}, {year}"
    return band, date


def scrape_rumba():
    response = requests.get("https://www.centralsaloon.com/events", headers=HEADERS)
    source = response.text
    extractor = selectorlib.Extractor.from_yaml_file("extract_rumba.yaml")


if __name__ == "__main__":
    scrape_central()


