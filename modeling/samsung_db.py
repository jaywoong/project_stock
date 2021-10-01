
# 기존 컬럼명
#'DATE', '거래량', 'PER','PBR','기관합계', '기타법인','개인','외국인합계', 'NASDAQ','S&P','CBOE', 'Exchange rate','futures2y','futures10y, 'y'
# 바뀐 컬럼명
# date, high, low, y, volume, atr / per, pbr, institution, corp, retail, foreign / nasdaq, sp, cboe, exchangerate, futures2y, futures10y,

import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pykrx import stock
import FinanceDataReader as fdr
from datetime import date, datetime, timedelta

class UpdateDB:
    def __init__(self):
        self.tday = date.today().strftime('%Y%m%d')  # 오늘
        self.yday = (date.today() - timedelta(1)).strftime('%Y%m%d')  # 어제
        self.bfyday = (date.today() - timedelta(2)).strftime('%Y%m%d')  # 그저께
        self.options = Options()
        self.options.add_argument('headless')
        self.contents = []

    def loadData(self):
        try:
            file = pd.read_excel('C:\Develops\mainproject_stock\modeling\data\samsung.xlsx')
        except FileNotFoundError as ex:
            print(ex)
        else:
            file.to_sql('samsung', conn, if_exists='append', index=False)


    def getKRX(self, code):
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
        return self.df_krx


    def getINVEST(self):
        try:
            self.sp500 = fdr.DataReader('US500', self.tday, self.tday, )[['Close']]
        except:
            print("거시경제지표 중 S&P500은 당일 저녁에 업데이트 됩니다.")
            self.sp500 = pd.DataFrame(columns=['sp'])
        self.cboe = fdr.DataReader('VIX', self.tday, self.tday, )[['Close']]
        self.rate = fdr.DataReader('USD/KRW', self.tday, self.tday, )[['Close']]
        df_invest = pd.concat([self.sp500, self.cboe, self.rate], axis=1).reset_index()
        df_invest.columns = ['date', 'sp', 'cboe', 'exchangerate']
        self.df_invest = df_invest.set_index('date')
        return self.df_invest


    def crawlINVEST(self):
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
        self.df_crawl = df_crawl.set_index('date')
        return self.df_crawl


    def saving(self):
        df = pd.merge(self.df_krx, self.df_invest, on='date')
        self.df_merge = pd.merge(df, self.df_crawl, on='date')
        self.df_merge.to_sql('samsung', conn, if_exists='append') # 테이블명
        conn.commit()
        conn.close()
        print('data inserted to DB.')


if __name__ == "__main__":
    conn = sqlite3.connect('samsung.db')
    c = conn.cursor()

    update = UpdateDB()  # 클래스 선언
    update.loadData()  # 기존 데이터 엑셀파일 db에 저장
    update.getKRX("005930")  # y, volume, per, pbr, institution, corp, retail, foreign
    update.getINVEST()  # sp, cboe, exchangerate
    update.crawlINVEST()  # nasdaq, futures2y, futures10y
    update.saving()  # db에 최종 저장

