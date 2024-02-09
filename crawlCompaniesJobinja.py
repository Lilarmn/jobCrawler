import pandas as pd
from bs4 import BeautifulSoup
import requests as rq
from concurrent.futures import ThreadPoolExecutor
from time import sleep
import pyodbc
from configs import *
from random import choice

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
        print(f'{self.counter} pages start')
        soup = BeautifulSoup(html_doc ,'html.parser')

        links_in_page = soup.find_all('a',{
            'class':'c-companyOverview'
        })
        links_in_page = list(map(lambda x:x.get('href') ,links_in_page))

        def check_value_of_links(url):
        
            if url.split('/')[-1] != 'jobs':
                return True
            else:
                return False
        links_in_page = list(filter(lambda x:check_value_of_links(x),links_in_page))
        self.links.extend(links_in_page)
        self.counter += 1
        print(f'{self.counter} pages finish ------')

    def worker(self,url):
        html_doc = self.send_request(url)
        if html_doc:
            self.parse_page(html_doc)
        else:
            print(f'{url} failed')

    @staticmethod
    def connect_cursor():
        conn = pyodbc.connect(f'DRIVER={DRIVER};' +
                              f'SERVER={SERVER};'+
                              f'DATABASE={DATABASE};'+
                              f'UID={UID};'+
                              f'PWD={PWD}')
        cursor = conn.cursor()
        return conn ,cursor

    def run_threads(self):

        max_threads = 10
        urls = [f"{self.mainUrl}?page={i}" for i in range(1, self.n_page)]

        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            executor.map(self.worker, urls)

        conn,cursor = self.connect_cursor()
        query = """
        IF NOT EXISTS (SELECT 1 FROM CrawlData..jobinja_companies WHERE link = ?)
        BEGIN
            INSERT INTO CrawlData..jobinja_companies (link)
            VALUES (?)
        END
        """
        for link in self.links:
            cursor.execute(query,(link,link,))

        cursor.commit()
        conn.close()


class CrawlPage(CrawlCompanies):
    def __init__(self,):
        super().__init__('#',1)
        self.job_details = []

    def find_all_jobs_links(self,company_url):

        if company_url.split('/')[-1] != 'jobs' :
            company_url = company_url + '/jobs'

        html_doc = self.send_request(company_url)
        soup = BeautifulSoup(html_doc , 'html.parser')
        job_links = soup.find_all('a',class_='c-jobListView__titleLink')
        job_links = list(map(lambda x:x.get('href') , job_links))

        return job_links

    def parse_job_page(self,job_link):

        html_doc = self.send_request(job_link)
        soup = BeautifulSoup(html_doc, 'html.parser')
        if soup.find('div',class_='tags') and soup.find('h4',class_='c-infoBox__itemTitle'):

            company = job_link.split('/')[4]

            job_title = soup.find('div',
                                        class_='c-jobView__titleText').text.replace('\n','').strip()

            tags_title = soup.find_all('h4', class_='c-infoBox__itemTitle')
            tags_title = list(map(lambda x: x.text.replace('\n','').strip().replace('\u200c',' '), tags_title))

            tags_results = soup.find_all('div',class_='tags')
            tags_results = list(map(lambda x: x.text.replace('\n','').strip().replace('\u200c',' '), tags_results))

            tags_dict2 = dict(zip(tags_title,tags_results))

            return company,job_title,tags_dict2

    def get_links_from_database(self):
        conn ,cursor = self.connect_cursor()
        query = """
            select top(4)* from CrawlData..jobinja_companies
        """
        cursor.execute(query)
        links = cursor.fetchall()
        cursor.close()
        conn.close()
        return links

    def worker(self,url):
        jobs = self.find_all_jobs_links(url[0])
        for job in jobs:
            detail = self.parse_job_page(job)
            print(detail)
            self.job_details.append(detail)

    def run_threads(self):
        max_threads = 10
        urls = self.get_links_from_database()
        print(urls)
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            executor.map(self.worker, urls)


        conn , cursor = self.connect_cursor()
        insert_query = '''
        INSERT INTO [CrawlData].[dbo].[jobinja]
                   ([company]
                   ,[title]
                   ,[location]
                   ,[category]
                   ,[essentials]
                   ,[salary]
                   ,[experience]
                   ,[type_of_work]
                   ,[studies]
                   ,[military]
                   ,[gender])
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''

        for detail in self.job_details:
            print(detail)
            cursor.execute(
                insert_query,
                (
                    detail[0],
                    detail[1],
                    detail[2].get('موقعیت مکانی',None),
                    detail[2].get('دسته بندی شغلی',None),
                    detail[2].get('مهارت های مورد نیاز',None),
                    detail[2].get('حقوق',None),
                    detail[2].get('حداقل سابقه کار',None),
                    detail[2].get('نوع همکاری',None),
                    detail[2].get('حداقل مدرک تحصیلی',None),
                    detail[2].get('وضعیت نظام وظیفه',None),
                    detail[2].get('جنسیت',None)
                )
            )
            print('one row added')

        conn.commit()
        cursor.close()
        conn.close()
