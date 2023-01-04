from bs4 import BeautifulSoup
from urllib.parse import urlparse

import time
import settings
import requests
import sys
import json

def get_all_postings_from_url():
    """
    Scrapes Craigslist and finds the latest listings.
    :return: A list of actually new results.
    """
    
    results = []
    for url in settings.LISTING_URLS:
        r = requests.get(url)
        response = r.text
        soup = BeautifulSoup(response, "html.parser")
        # links = soup.find_all('p', {'class':'result-info'})

        print(soup)

        # for link in links:
        #     title = link.find('a', {'class':'result-title'})
        #     meta = link.find('span', {'class':'result-meta'})
        #     price = meta.find('span', {'class':'result-price'})
        #     date = link.find('time', {'class':'result-date'})

        #     # Skip out of region postings
        #     if( title['href'].startswith('//') is True or title['href'].startswith('http')):
        #         continue

        #     result = {}
        #     result['name'] = title.text
        #     result['id'] = title['data-id']

        #     # Get domain from url
        #     parsed_uri = urlparse( url )
        #     domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)            
        #     result['url'] = domain + title['href']
            
        #     result['datetime'] = date['datetime']
            
        #     if price is not None:
        #         result['price'] = price.text
        #     else:
        #         result['price'] = ''

        #     results.append(result)

    return results


if __name__ == "__main__":
    postings = get_all_postings_from_url()

