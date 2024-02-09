from crawlCompaniesJobinja import CrawlCompanies , CrawlPage
from glob import glob

if __name__ == '__main__':
    # obj = CrawlCompanies('https://jobinja.ir/companies', 15)
    # print(obj.run_threads())
    # files = glob('links.xlsx')
    # if not files:
    #     pass
    #     obj = CrawlCompanies('https://jobinja.ir/companies',1)
    #     print(obj.run_threads())
    # else:
    #     obj2 = CrawlPage()
    #     a = obj2.parse_job_page('https://jobinja.ir/companies/asa-1/jobs/Atah/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%DA%A9%D8%A7%D8%B1%D8%B4%D9%86%D8%A7%D8%B3-%D9%BE%D8%A7%DB%8C%DA%AF%D8%A7%D9%87-%D8%AF%D8%A7%D8%AF%D9%87-sql-server-dba-%D8%AF%D8%B1-%D9%88%DB%8C%D8%B3%D8%AA%D8%A7-%D8%B3%D8%A7%D9%85%D8%A7%D9%86%D9%87-%D8%A2%D8%B3%D8%A7')
    #     for i,v in a.items():
    #         print(i, ' : ',v)
    obj = CrawlPage()
    print(obj.run_threads())
