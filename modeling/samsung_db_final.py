
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


def loadData():
    try:
        file = pd.read_excel('C:\Develops\mainproject_stock\modeling\data\samsung.xlsx')
    except FileNotFoundError as ex:
        print(ex)
    else:
        file.to_sql('samsung', conn, if_exists='append')

def getDate():
    global end, start
    end = date.today().strftime('%Y%m%d')  # 오늘
    start = (date.today() - timedelta(1)).strftime('%Y%m%d')  # 어제
    return end, start

def getKRX(code):
    global volume, per, value
    try:
        volume = stock.get_market_ohlcv_by_date(start, end, code)[['종가', '거래량']]
        per = stock.get_market_fundamental_by_date(start, end, code)[['PER', 'PBR']]
        value = stock.get_market_trading_value_by_date(start, end, code).drop(['전체'], axis=1)
        # 개별주관련지표 중 기관합계, 기타법인, 개인, 외국인합계는 데이터 업데이트가 늦음
    except:
        pass
    df = pd.concat([volume, per, value], axis=1)
    df_krx = df.reset_index()
    df_krx.columns = ['date', 'y', 'volume', 'per', 'pbr', 'institution', 'corp', 'retail', 'foreign']
    df_krx = df_krx.set_index('date')
    return df_krx


def getINVEST():
    global sp500, cboe, rate
    try:
        sp500 = fdr.DataReader('US500', start, end)[['Close']]
        cboe = fdr.DataReader('VIX', start, end)[['Close']]
        rate = fdr.DataReader('USD/KRW', start, end)[['Close']]
        # 거시경제지표 중 S&P500은 데이터 업데이트가 늦음
    except:
        pass
    df = pd.concat([sp500, cboe, rate], axis=1)
    df_invest = df.reset_index()
    df_invest.columns = ['date', 'sp', 'cboe', 'exchangerate']
    df_invest = df_invest.set_index('date')
    return df_invest

def crawlINVEST():
    global contents
    options = Options()
    options.add_argument('headless')
    contents = []
    urls = ['https://kr.investing.com/indices/nasdaq-composite-historical-data','https://kr.investing.com/rates-bonds/us-2-yr-t-note-historical-data', 'https://kr.investing.com/rates-bonds/us-10-yr-t-note-historical-data']
    for url in urls:
        driver = webdriver.Chrome('C:\chromedriver.exe', options=options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        try:
            index = soup.select('#last_last')
            contents.append(index[0].text.strip())
        except:
            driver.execute_script("window.scrollTo(0, 700)")
            index = soup.select('#curr_table > tbody > tr:nth-child(1) > td:nth-child(2)')
        del soup
        driver.quit()
    date = pd.DatetimeIndex([datetime.today().date()])
    df = pd.DataFrame([contents], date, ['nasdaq','futures2y', 'futures10y'])
    df = df.reset_index().rename(columns={'index': 'date'})
    df_crawl = df.set_index('date')
    return df_crawl

def saving(final):
    final.to_sql('samsung', conn, if_exists='append') # 테이블명
    conn.commit()
    conn.close()
    print('data inserted to DB.')


if __name__ == "__main__":
    conn = sqlite3.connect('samsung.db')
    c = conn.cursor()

    loadData()  # 기존 데이터 들어있는 엑셀파일 db에 저장
    getDate()  # 오늘, 어제 날짜
    krx = getKRX("005930")  # y, volume, per, pbr, institution, corp, retail, foreign
    invest = getINVEST()  # sp, cboe, exchangerate
    crawl = crawlINVEST()  # nasdaq, futures2y, futures10y

    df = pd.merge(krx, invest, on='date')
    df_merge = pd.merge(df, crawl, on='date')
    saving(df_merge)  # db에 최종 저장




