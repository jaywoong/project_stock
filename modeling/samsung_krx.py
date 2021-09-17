import pandas as pd
import sqlite3
from pykrx import stock
from datetime import date, timedelta

conn = sqlite3.connect('samsung.db')  # db파일 생성
c= conn.cursor()  # db에 연결하는 cursor

#c.execute("CREATE TABLE IF NOT EXISTS samsung (id INTEGER PRIMARY KEY AUTOINCREMENT, DATE REAL, 거래량 REAL, PER REAL, PBR REAL, 기관합계 REAL, 기타법인 REAL, 개인 REAL, 외국인합계 REAL)")
# 내가 연결한 db파일에 TABLE 생성

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

    def saving(self, code):
        self.df = pd.concat([self.volume, self.per, self.value], axis=1)
        self.df.to_sql('samsung', conn, if_exists='replace')
        conn.commit()  # db에 저장



if __name__ == "__main__":
    code = "005930"  # 종목코드
    krx = KRX()
    krx.getDate()
    krx.getStock(code)
    krx.saving(code)

    conn.close()


