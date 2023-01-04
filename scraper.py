from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from settings import LISTING_URL

import time
import requests
import sys
import json
from pprint import pprint

def get_all_postings_from_url(url):
    """
    Scrapes Craigslist and finds the latest listings.
    :return: A list of actually new results.
    """
    
    # r = requests.get(url)
    # response = r.text
    # soup = BeautifulSoup(response, "html.parser")

    browser = webdriver.Chrome('chromedriver')
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('--enable-javascript')
    options.add_argument("--headless")
    browser.get(url)
    time.sleep(10000)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    pprint(soup)


    return


if __name__ == "__main__":
    get_all_postings_from_url(LISTING_URL)

