import pandas as pd
from bs4 import BeautifulSoup
import requests as rq
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import choice
# import pandas as pd

class CrawlCompanies:
    def __init__(self,url,number_of_page):
        self.mainUrl = url
        self.links = []
        self.n_page = number_of_page
        self.counter = 0

    @staticmethod
    def send_request(url):
        response = rq.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print('request failed')
            return None
    def parse_page(self,html_doc):
        soup = BeautifulSoup(html_doc ,'html.parser')

        links_in_page = soup.find_all('a',{
            'class':'c-companyOverview'
        })
        links_in_page = list(map(lambda x:x.get('href') ,links_in_page))

        self.links.extend(links_in_page)
        self.counter += 1
        print(f'{self.counter} pages done')


    def worker(self,url):
        html_doc = self.send_request(url)
        if html_doc:
            self.parse_page(html_doc)
        else:
            print(f'{url} failed')

    def run_threads(self):

        max_threads = 10
        urls = [f"{self.mainUrl}?page={i}" for i in range(1, self.n_page)]

        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            executor.map(self.worker, urls)

        series = pd.Series(self.links,name='links')
        df = series.to_frame()
        df.to_excel('newlinks.xlsx', index=False)



