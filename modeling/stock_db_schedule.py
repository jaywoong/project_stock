
# 기존 컬럼명
#'DATE', '거래량', 'PER','PBR','기관합계', '기타법인','개인','외국인합계', 'NASDAQ','S&P','CBOE', 'Exchange rate','futures2y','futures10y, 'y'
# 바뀐 컬럼명
# date, volume, per, pbr, institution, corp, retail, foreign, nasdaq, sp, cboe, exchangerate, futures2y, futures10y, y

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
        self.tday = date.today().strftime('%Y%m%d')  # 오늘
        self.yday = (date.today() - timedelta(1)).strftime('%Y%m%d')  # 어제
        self.bfyday = (date.today() - timedelta(2)).strftime('%Y%m%d')  # 그저께
        self.options = Options()
        self.options.add_argument('headless')
        self.contents = []

    def getINVEST(self):  # Investing.com 데이터
        try:
            self.sp500 = fdr.DataReader('US500', self.yday, self.tday,)[['Close']]
            self.cboe = fdr.DataReader('VIX', self.yday, self.tday,)[['Close']]
            self.rate = fdr.DataReader('USD/KRW', self.yday, self.tday,)[['Close']]
        except:
            self.sp500 = pd.DataFrame(columns=['close'])
            self.cboe = pd.DataFrame(columns=['close'])
            self.rate = pd.DataFrame(columns=['close'])
            # 거시경제지표 중 S&P500은 데이터 업데이트가 늦음
        df_index = pd.concat([self.sp500, self.cboe, self.rate], axis=1).reset_index()
        df_index.columns = ['date', 'sp', 'cboe', 'exchangerate']
        self.df_index = df_index.set_index('date')
        print('getINVEST complete.')
        return self.df_index

    def crawlINVEST(self):  # Investing.com 크롤링
        self.getINVEST()
        self.urls = ['https://kr.investing.com/indices/nasdaq-composite-historical-data','https://kr.investing.com/rates-bonds/us-2-yr-t-note-historical-data', 'https://kr.investing.com/rates-bonds/us-10-yr-t-note-historical-data']
        for url in self.urls:
            self.driver = webdriver.Chrome('C:\chromedriver.exe', options=self.options)
            self.driver.get(url)
            self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            try:
                self.index = self.soup.select('#last_last')
                self.contents.append(self.index[0].text.strip())
            except:
                self.driver.execute_script("window.scrollTo(0, 700)")
                self.index = self.soup.select('#curr_table > tbody > tr:nth-child(1) > td:nth-child(2)')
            del self.soup
            self.driver.quit()
        self.dateindex = pd.DatetimeIndex([datetime.today().date()])
        df_crawl = pd.DataFrame([self.contents], self.dateindex, ['nasdaq','futures2y', 'futures10y']).reset_index().rename(columns={'index': 'date'})
        self.df_crawl = pd.DataFrame([self.contents],['nasdaq', 'futures2y', 'futures10y'])
        self.df_crawl = df_crawl.set_index('date')
        print('crawlINVEST complete.')
        return self.df_crawl

    def mergeINVEST(self):
        self.crawlINVEST()
        self.df_invest = pd.merge(self.df_index, self.df_crawl, on='date')
        return self.df_invest

    def getKRX(self, code):  # KRX 데이터
        self.stockname = stock.get_market_ticker_name(code)
        def getATR():
            df_atr = stock.get_market_ohlcv_by_date(self.bfyday, self.tday, code).drop(['시가', '거래량'], axis=1)
            a = df_atr['고가'][0] - df_atr['저가'][0]  # 고가-저가
            b = df_atr['고가'][0] - df_atr['종가'][1]  # 고가-전날종가
            c = df_atr['저가'][0] - df_atr['종가'][1]  # 저가-전날종가
            lst = [abs(a), abs(b), abs(c)]
            return max(lst)
        self.ohlcv = stock.get_market_ohlcv_by_date(self.yday, self.tday, code)[['종가', '거래량']]
        self.ohlcv['ATR'] = getATR()
        self.per = stock.get_market_fundamental_by_date(self.tday, self.tday, code)[['PER', 'PBR']]
        try:
            self.value = stock.get_market_trading_value_by_date(self.tday, self.tday, code).drop(['전체'], axis=1)
        except:
            print('개별주관련지표 중 기관합계,기타법인,개인,외국인합계는 당일 16:30쯤 업데이트 됩니다.')
            self.value = pd.DataFrame(columns=['institution', 'corp', 'retail', 'foreign'])
        df_krx = pd.concat([self.ohlcv, self.per, self.value], axis=1).reset_index()
        df_krx.columns = ['date', 'y', 'volume', 'atr', 'per', 'pbr', 'institution', 'corp', 'retail', 'foreign']
        self.df_krx = df_krx.set_index('date')
        print('{} getKRX complete.'.format(self.stockname))
        return self.df_krx

    def saving(self):  # 데이터 합쳐서 db에 저장
        self.df_merge = pd.merge(self.df_krx, self.df_invest, on='date')
        self.df_merge.to_sql('{}'.format(self.stockname), conn, if_exists='append') # 테이블명
        conn.commit()
        print('{} inserted to DB.'.format(self.stockname))



if __name__ == "__main__":
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()

    def update():
        updatedb = UpdateDB()  # 클래스 선언
        updatedb.mergeINVEST()   # sp, cboe, exchangerate, nasdaq, futures2y, futures10y

        # codes = ['005930', '000660', '051910', '066570', '011070', '018260', '009150', '032830',
        #          '000810', '017670', '030200', '000720', '028050', '003490', '005380', '000270',
        #          '271560', '097950', '007310', '006800', '071050', '005940', '051900', '090430',
        #          '002790', '035250', '008770', '105560', '055550', '086790', '023530', '139480',
        #          '004170', '007070', '035420', '035720', '035760', '253450', '207940', '068270',
        #          '128940', '036570', '251270', '009830', '006260', '005490', '010130', '010950',
        #          '096770', '011200']
        codes = ['005930','000660']
        for code in codes:
            updatedb.getKRX(code)  # y, volume, per, pbr, institution, corp, retail, foreign
            updatedb.saving()  # db에 최종 저장
        conn.close()

    schedule.every(1).minutes.do(update)  # 1분마다 동작
    #schedule.every().day.at("5:30").do(update)  # 매일 5:30에 동작
    while True:
        schedule.run_pending()
        time.sleep(1)

