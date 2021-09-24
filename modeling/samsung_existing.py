import pandas as pd
import sqlite3

conn = sqlite3.connect('samsung.db')  # db파일 생성
c= conn.cursor()  # db에 연결하는 cursor

#c.execute("CREATE TABLE IF NOT EXISTS samsung (id INTEGER PRIMARY KEY AUTOINCREMENT, DATE REAL, 거래량 REAL, PER REAL, PBR REAL, 기관합계 REAL, 기타법인 REAL, 개인 REAL, 외국인합계 REAL)")
# 내가 연결한 db파일에 TABLE 생성

df_excel = pd.read_excel('C:\Develops\mainproject_stock\modeling\data\samsung.xlsx')
df_excel.to_sql('samsung', conn, if_exists='replace')