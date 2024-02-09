import requests as rq
from bs4 import BeautifulSoup


class Crawl:
    def __init__(self ,url):
        self.url = url

    @staticmethod
    def make_csv_file():
        with open('data.csv',mode='w') as f:
            f.write('')
    def send_request(self,url):
        response = rq.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def make_soup(self ,html_doc):
        soup = BeautifulSoup(html_doc ,'html.parser')
        return soup

    def url_generator(self ,extend_part):
        return self.url + f'/{extend_part}/'

    def parse_job_div(self):

        for i in range(600_080,600_100):
            url = self.url_generator(i)
            html_doc = self.send_request(url)
            if html_doc:
                soup = self.make_soup(html_doc)
                header = soup.find('div',
                                   attrs={'class':'text-black font-size-1 font-weight-bold py-2 yn_title'}).text
                print(header ,'---->' , url)
                self.parse_job_description(url)
            else:
                print(url , 'Failed')

    def parse_job_description(self,job_url):
        html_doc = self.send_request(job_url)
        soup = BeautifulSoup(html_doc ,'html.parser')

        job_title = soup.find('div',
                              attrs={'class': 'text-black font-size-1 font-weight-bold py-2 yn_title'}).text.strip()
        print(job_title)

        company_title = soup.find('a',
                              attrs={'class': 'text-primary font-size-2 font-weight-bold px-0 py-2 d-flex align-items-center yn_brand'}).text.strip()
        print(company_title)

        location = soup.find('div',attrs={'class':'text-muted'}).getText().strip()
        print(location)

        main_indicators_list = soup.find_all("span" ,attrs={"class":"col mr-2 px-0 word-break"})

        main_indicators = ""
        for i in main_indicators_list:
            main_indicators = main_indicators + " / " + i.text

        print(main_indicators)

        description = soup.find('div',attrs={'class':'col-12 row text-black px-0 mb-3'}).text

        data = ','.join([job_title,company_title, location, main_indicators, description, job_url])
        with open('data.csv', mode='a', encoding='utf-8') as f:
            f.writelines(data + '\n')
        print('one row affect')



