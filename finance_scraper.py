import requests
import pandas
from contextlib import contextmanager
from bs4 import BeautifulSoup

MAIN_SITE = "https://www.mygemel.net"

class FundScraper:
    def __init__(self, typee, course, name):
        self.typee, self.course, self.name = typee, course, name
        self.current_page = None
        self.previous_pages = []

    @contextmanager
    def set_current_page(self, new_page):
        self.previous_pages.append(self.current_page)
        try:
            self.current_page = BeautifulSoup(requests.get(new_page).text, 'html.parser')
            yield

        except requests.exceptions.MissingSchema as e:
            print(f'Error: No Page Found.')
        finally:
            self.current_page = self.previous_pages.pop()

    def extract_fund_link_page(self):
        for title in self.current_page.find_all("div", {"class": "koteret"}):
            if self.typee in title.h2.text:
                return title.a.get('href')

    def extract_fund_name_link_page(self):
        for fund_course in self.current_page.find_all("caption"):
            if self.course in fund_course.h2.text:
                for table_entry in fund_course.find_next_sibling("tbody").find_all("tr"):
                    if self.name in table_entry.td.a.text:
                        return "/".join([MAIN_SITE, table_entry.td.a.get('href')])

    def extract_fund_data(self):
        output, columns = [], []
        for entry in self.current_page.find(text='תשואות:').find_next('ul').find_all('li'):
            columns.append(entry.text.split(":")[0])
            output.append(entry.text.split(":")[1])
        
        return pandas.DataFrame([output], columns=columns)

    def get_roi_data(self):
        with self.set_current_page(MAIN_SITE):
            fund_page_link = self.extract_fund_link_page()

            with self.set_current_page(fund_page_link):
                fund_name_page_link = self.extract_fund_name_link_page()
                
                with self.set_current_page(fund_name_page_link):
                    return self.extract_fund_data()
