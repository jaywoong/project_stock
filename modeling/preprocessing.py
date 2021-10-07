import schedule
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

class Preprocessing:
    def job(self):
        nasdaq = pd.read_csv('./data/나스닥종합지수 내역.csv')
        nasdaq_copy = nasdaq[['날짜', '종가']].copy()
        nasdaq_copy.columns = ['DATE', 'NASDAQ']

        sap = pd.read_csv('./data/S&P 500 내역.csv')
        sap_copy = sap[['날짜', '종가']].copy()
        sap_copy.columns = ['DATE', 'S&P']

        merge_data = pd.merge(nasdaq_copy, sap_copy, on='DATE', how='outer')
        CBOE = pd.read_csv('./data/CBOE Volatility Index 내역.csv')
        CBOE_copy = CBOE[['날짜', '종가']].copy()
        CBOE_copy.columns = ['DATE', 'CBOE']

        merge_data = pd.merge(merge_data, CBOE_copy, on='DATE', how='outer')
        exchange = pd.read_csv('./data/USD_KRW 내역.csv')
        exchange_copy = exchange[['날짜', '종가']].copy()
        exchange_copy.columns = ['DATE', 'Exchange rate']

        merge_data = pd.merge(merge_data, exchange_copy, on='DATE', how='outer')
        futures2y = pd.read_csv('./data/2년만기 미국채 선물 역사적 데이터.csv')
        futures2y_copy = futures2y[['날짜', '종가']].copy()
        futures2y_copy.columns = ['DATE', 'futures2y']

        merge_data = pd.merge(merge_data, futures2y_copy, on='DATE', how='outer')
        futures10y = pd.read_csv('./data/10년만기 미국채 선물 역사적 데이터.csv')
        futures10y_copy = futures10y[['날짜', '종가']].copy()
        futures10y_copy.columns = ['DATE', 'futures10y']

        merge_data = pd.merge(merge_data, futures10y_copy, on='DATE', how='outer')

        merge_data = merge_data.sort_values(by=['DATE'], axis=0)
        merge_data.to_csv('./data/merge_data_test.csv', index=False)

        #enp

        df1 = pd.read_excel('./data/시세추이.xlsx')
        df_atr = df1.iloc[:,[0,1,5,6]]
        df_atr.columns = ['date', 'fin', 'high', 'low']

        lst = []
        atr = []

        for i in range(0,len(df_atr)-1):
            a = df_atr.iloc[i,2] - df_atr.iloc[i,3]
            b = df_atr.iloc[i,2] - df_atr.iloc[i+1,1]
            c = df_atr.iloc[i,3] - df_atr.iloc[i+1,1]
            lst = [abs(a),abs(b),abs(c)]
            atr.append(max(lst))

        fin = list(df_atr[0:-1]['fin'])
        #del fin[820:823] # 거래정지 시점 데이터 행 삭제

        df1 = df1.drop(len(df1)-1,axis=0)
        df1 = df1[['일자', '거래량']]
        df2 = pd.read_excel('./data/PERPBR.xlsx')
        df2 = df2[['일자', 'PER', 'PBR']]
        df3 = pd.read_excel('./data/거래실적.xlsx')
        df3 = df3.drop(columns=['전체'], axis=1)

        enp = pd.merge(df1, df2, on='일자', how='outer')
        enp = pd.merge(enp, df3, on='일자', how='outer')
        enp['ATR'] = atr

        enp['일자'] = pd.to_datetime(enp['일자'])
        enp.rename(columns={'일자':'DATE'}, inplace=True)
        macro_data = pd.read_csv('./data/merge_data.csv')
        macro_data['DATE'] = pd.to_datetime(macro_data['DATE'])
        macro_data = macro_data.dropna(axis=0)
        df_enp = pd.merge(enp, macro_data, how='left', on='DATE')

        df_enp['y'] = fin
        df_enp.sort_values('DATE', inplace=True)
        df_enp.fillna(method='ffill', inplace=True)

        df_enp.to_excel('./data/samsung_test.xlsx',index=False)

        r_csv = pd.read_csv("./data/merge_data.csv")
        save_xlsx = pd.ExcelWriter("./data/merge_data.xlsx")
        r_csv.to_excel(save_xlsx, index = False)

        save_xlsx.save()

        #xlsx파일 합치기
        excel_names = ['./data/merge_data.xlsx', './data/samsung_test.xlsx']
        excels = [pd.ExcelFile(name) for name in excel_names]
        frames = [x.parse(x.sheet_names[0], header = None, index_col = None) for x in excels]

        frames[1:] = [df[1:] for df in frames[1:]]
        combined = pd.concat(frames, axis=1)

        #저장
        combined.to_excel("./data/stock.xlsx")
    
