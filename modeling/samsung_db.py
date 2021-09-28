import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pykrx import stock
import FinanceDataReader as fdr
from datetime import date, datetime, timedelta

# class EXIST:
#     def getData(self):
#         self.df_excel = pd.read_excel('C:\Develops\mainproject_stock\modeling\data\samsung.xlsx')
#         self.df_excel.to_sql('samsung', conn, if_exists='append')


class KRX:
    def getDate(self):
        self.end = date.today().strftime('%Y%m%d')  # 오늘
        self.start = (date.today() - timedelta(1)).strftime('%Y%m%d')  # 어제

    def getStock(self, code):
        self.volume = stock.get_market_ohlcv_by_date(self.start, self.end, code)
        self.volume = self.volume[['거래량']]
        self.per = stock.get_market_fundamental_by_date(self.start, self.end, code)
        self.per = self.per[['PER', 'PBR']]
        self.v = stock.get_market_trading_value_by_date(self.start, self.end, code)
        self.value = self.v.drop(['전체'], axis=1)

    def saving(self):
        self.df = pd.concat([self.volume, self.per, self.value], axis=1)
        self.df_krx = self.df.reset_index()
        self.df_krx.columns=['date', 'volume', 'per', 'pbr', 'institution', 'corp', 'retail', 'foreign']
        self.df_krx = self.df_krx.set_index('date')
        self.df_krx.to_sql('samsung', conn, if_exists='append') # 테이블명
        conn.commit()  # db에 저장


class INVESTING:
    def getDate(self):
        self.end = date.today().strftime('%Y%m%d')  # 오늘
        self.start = (date.today() - timedelta(1)).strftime('%Y%m%d')  # 어제

    def getStock(self):
        self.sp500 = fdr.DataReader('US500', self.start, self.end)
        self.sp500 = self.sp500[['Close']]
        self.cboe = fdr.DataReader('VIX', self.start, self.end)
        self.cboe = self.cboe[['Close']]
        self.rate = fdr.DataReader('USD/KRW', self.start, self.end)
        self.rate  = self.rate[['Close']]

    def saving(self):
        self.df = pd.concat([self.sp500, self.cboe, self.rate], axis=1)
        self.df_invest = self.df.reset_index()
        self.df_invest.columns = ['date', 'sp', 'cboe', 'exchangerate']
        self.df_invest = self.df_invest.set_index('date')
        self.df_invest.to_sql('samsung', conn, if_exists='append')
        conn.commit()  # db에 저장


class INVESTINGCRAWL:
    def __init__(self):
        self.contents = []
        self.options = Options()
        self.options.add_argument('headless')

    def crawling(self, url):
        self.driver = webdriver.Chrome('C:\chromedriver.exe', options=self.options)
        self.driver.get(url)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.index = self.soup.select('#last_last')
        self.contents.append(self.index[0].text.strip())
        del self.soup
        self.driver.quit()

    def saving(self):
        self.date = pd.DatetimeIndex([datetime.today().date()])
        self.df = pd.DataFrame([self.contents], self.date, ['futures2y', 'futures10y'])
        self.df = self.df.reset_index().rename(columns={'index': 'date'})
        self.df_crawl = self.df.set_index('date')
        self.df_crawl.to_sql('samsung', conn, if_exists='append')
        conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect('samsung.db')  # db파일 생성
    c = conn.cursor()  # db에 연결하는 cursor
    # ex = EXIST()

    code = "005930"  # 종목코드
    krx = KRX()
    krx.getDate()
    krx.getStock(code)
    krx.saving()

    invest = INVESTING()
    invest.getDate()
    invest.getStock()
    invest.saving()

    crawl = INVESTINGCRAWL()
    us2yr = 'https://kr.investing.com/rates-bonds/us-2-yr-t-note-historical-data'
    crawl.crawling(us2yr)
    us10yr = 'https://kr.investing.com/rates-bonds/us-10-yr-t-note-historical-data'
    crawl.crawling(us10yr)
    crawl.saving()

    conn.close()


