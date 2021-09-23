import pandas as pd
import sqlite3
from pykrx import stock
import FinanceDataReader as fdr
from datetime import date, timedelta

conn = sqlite3.connect('samsung.db')  # db파일 생성
c= conn.cursor()  # db에 연결하는 cursor


class KRX:
    def getDate(self):
        self.end = date.today().strftime('%Y%m%d')  # 오늘
        self.start = (date.today() - timedelta(1)).strftime('%Y%m%d')  # 어제

    def getStock(self, code):
        self.volume = stock.get_market_ohlcv_by_date(self.start, self.end, code)
        self.volume = self.volume[['거래량']]

        self.per = stock.get_market_fundamental_by_date(self.end, self.end, code)
        self.per = self.per[['PER', 'PBR']]

        self.value = stock.get_market_trading_value_by_date(self.end, self.end, code)
        self.value = self.value.drop(['전체'], axis=1)

    def saving(self):
        self.df = pd.concat([self.volume, self.per, self.value], axis=1)
        self.df.to_sql('samsung', conn, if_exists='replace') # 테이블명
        conn.commit()  # db에 저장


class INVESTING:
    def getDate(self):
        self.end = date.today().strftime('%Y%m%d')  # 오늘
        self.start = (date.today() - timedelta(1)).strftime('%Y%m%d')  # 어제

    def getStock(self):
        self.sp500 = fdr.DataReader('US500', self.start, self.end)
        self.sp500 = self.sp500[['Close']].rename(columns={'Close':'S&P'})

        self.cboe = fdr.DataReader('VIX', self.start, self.end)
        self.cboe = self.cboe[['Close']].rename(columns={'Close':'CBOE'})

        self.rate = fdr.DataReader('USD/KRW', self.start, self.end)
        self.rate  = self.rate[['Close']].rename(columns={'Close':'Exchange rate'})

    def saving(self):
        self.df = pd.concat([self.sp500, self.cboe, self.rate], axis=1)
        self.df.to_sql('samsung', conn, if_exists='replace')
        conn.commit()  # db에 저장


if __name__ == "__main__":
    code = "005930"  # 종목코드
    krx = KRX()
    krx.getDate()
    krx.getStock(code)
    krx.saving()

    invest = INVESTING()
    invest.getDate()
    invest.getStock()
    invest.saving()

    conn.close()


