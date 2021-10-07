
# 기존 컬럼명
#'DATE', '거래량', 'atr', 'PER','PBR','기관합계', '기타법인','개인','외국인합계', 'NASDAQ','S&P','CBOE', 'Exchange rate','futures2y','futures10y, 'y'
# 바뀐 컬럼명
# date, volume, atr, per, pbr, institution, corp, retail, foreign, nasdaq, sp, cboe, exchangerate, futures2y, futures10y, y


import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pykrx import stock
import FinanceDataReader as fdr
from datetime import date, datetime, timedelta
import schedule
import time

class UpdateDB:
    def __init__(self):
        self.conn = sqlite3.connect('samsung.db')  # stock.db
        self.c = self.conn.cursor()
        self.yday = (date.today() - timedelta(1)).strftime('%Y%m%d')  # 1일 전
        self.bfyday = (date.today() - timedelta(2)).strftime('%Y%m%d')  # 2일 전
        self.bffyday = (date.today() - timedelta(3)).strftime('%Y%m%d')  # 3일 전
        self.options = Options()
        self.options.add_argument('headless')
        self.contents = []

    def getINVEST(self):  # Investing.com 데이터
        self.sp500 = fdr.DataReader('US500', self.yday, self.yday)[['Close']]
        self.cboe = fdr.DataReader('VIX', self.yday, self.yday)[['Close']]
        self.rate = fdr.DataReader('USD/KRW', self.yday, self.yday)[['Close']]
        # 거시경제지표 중 S&P500은 데이터 업데이트가 늦음
        df_index = pd.concat([self.sp500, self.cboe, self.rate], axis=1).reset_index()
        df_index.columns = ['date', 'sp', 'cboe', 'exchangerate']
        self.df_index = df_index.set_index('date')
        print('getINVEST complete.')
        return self.df_index

    def crawlINVEST(self):  # Investing.com 크롤링
        self.getINVEST()
        self.urls = ['https://kr.investing.com/indices/nasdaq-composite-historical-data',
                     'https://kr.investing.com/rates-bonds/us-2-yr-t-note-historical-data',
                     'https://kr.investing.com/rates-bonds/us-10-yr-t-note-historical-data']
        for url in self.urls:
            self.driver = webdriver.Chrome('C:\chromedriver.exe', options=self.options)
            self.driver.get(url)
            self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            try:
                self.index = self.soup.select('#last_last')
            except:
                self.driver.execute_script("window.scrollTo(0, 700)")
                self.index = self.soup.select('#curr_table > tbody > tr:nth-child(1) > td:nth-child(2)')
            self.contents.append(self.index[0].text.strip())
            del self.soup
            self.driver.quit()
        self.dateindex = pd.DatetimeIndex([(date.today() - timedelta(1))])  # datetime.today().date()
        df_crawl = pd.DataFrame([self.contents], index=self.dateindex,
                                columns=['nasdaq', 'futures2y', 'futures10y']).reset_index().rename(
            columns={'index': 'date'})
        self.df_crawl = df_crawl.set_index('date')
        print('crawlINVEST complete.')
        return self.df_crawl

    def mergeINVEST(self):
        self.crawlINVEST()
        self.df_invest = pd.merge(self.df_index, self.df_crawl, on='date')
        print(self.df_invest)
        return self.df_invest

    def getKRX(self, code):  # KRX 데이터
        self.stockname = stock.get_market_ticker_name(code)
        def getATR():
            df_a = stock.get_market_ohlcv_by_date(self.bffyday, self.yday, code)
            df_atr = df_a.rename(index={'날짜': 'Date'}).drop(columns="시가", axis=1)
            df_atr.columns = ['high', 'low', 'close', 'volume']
            df_atr["atr"] = ""
            lst = []
            atr = []
            for i in range(len(df_atr) - 1):
                a = df_atr.iloc[i, 0] - df_atr.iloc[i, 1]  # 고가-저가
                b = df_atr.iloc[i, 0] - df_atr.iloc[i + 1, 2]  # 고가-전날종가
                c = df_atr.iloc[i, 1] - df_atr.iloc[i + 1, 2]  # 저가-전날종가
                lst = [abs(a), abs(b), abs(c)]
                atr.append(max(lst))
            df_atr.iloc[1, 4] = atr
            df_atr = df_atr[1:]
            return df_atr[['close', 'volume', 'atr']]
        self.ohlcv = getATR()
        self.funda = stock.get_market_fundamental_by_date(self.yday, self.yday, code)[['PER', 'PBR']]
        self.value = stock.get_market_trading_value_by_date(self.yday, self.yday, code).drop(['전체'], axis=1)

        df = pd.concat([self.ohlcv, self.funda, self.value], axis=1)
        self.df_krx = df.reset_index()
        self.df_krx.columns = ['date', 'y', 'volume', 'atr', 'per', 'pbr', 'institution', 'corp', 'retail', 'foreign']
        self.df_krx = self.df_krx.set_index('date')
        print('{} getKRX complete.'.format(self.stockname))
        return self.df_krx

    def saving(self):  # 데이터 합쳐서 db에 저장
        self.df_merge = pd.merge(self.df_krx, self.df_invest, on='date')
        self.df_merge.to_sql('{}'.format(self.stockname), self.conn, if_exists='append') # 테이블명
        self.conn.commit()
        print('{} inserted to DB.'.format(self.stockname))


if __name__ == "__main__":
    def update():
        updatedb = UpdateDB()  # 클래스 선언
        updatedb.mergeINVEST()   # sp, cboe, exchangerate, nasdaq, futures2y, futures10y

        codes = ['005930', '000660', '051910', '066570', '011070', '018260', '009150', '032830',
                 '000810', '017670', '030200', '000720', '028050', '003490', '005380', '000270',
                 '271560', '097950', '007310', '006800', '071050', '005940', '051900', '090430',
                 '002790', '035250', '008770', '105560', '055550', '086790', '023530', '139480',
                 '004170', '007070', '035420', '035720', '035760', '253450', '207940', '068270',
                 '128940', '036570', '251270', '009830', '006260', '005490', '010130', '010950',
                 '096770', '011200']

        for code in codes:
            updatedb.getKRX(code)  # y, volume, per, pbr, institution, corp, retail, foreign
            updatedb.saving()  # db에 최종 저장

    # schedule.every(1).minutes.do(update)  # 1분마다 동작
    schedule.every().day.at("5:30").do(update)  # 매일 5:30에 동작
    while True:
        schedule.run_pending()
        time.sleep(1)

