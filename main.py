from crawlCompanies import CrawlCompanies

if __name__ == '__main__':
    obj = CrawlCompanies('https://jobinja.ir/companies',10416)
    print(obj.run_threads())
