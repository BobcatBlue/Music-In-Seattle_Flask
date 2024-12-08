import requests
import selectorlib
from lxml import html
from bs4 import BeautifulSoup
from datetime import datetime


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



def scrape_bmt(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    soup = BeautifulSoup(source, features="html.parser")
    print(soup.prettify())



if __name__ == "__main__":
    scrape_bmt("https://www.thebluemoonseattle.com/calendar")



