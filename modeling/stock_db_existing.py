
# 엑셀데이터 컬럼 통일하기
# date, volume, atr, per, pbr, institution, corp, retail, foreign, nasdaq, sp, cboe,
# exchangerate, futures2y, futures10y, y

import pandas as pd
import sqlite3

def loadData(stockname):  # 엑셀데이터 db에 저장
    try:
        file = pd.read_excel('../modeling/data/{}.xlsx'.format(stockname))
    except FileNotFoundError as ex:
        print(ex)
    else:
        file.to_sql('{}'.format(stockname), conn, if_exists='append')  # 기업마다 다른 테이블로 저장
        print('{} inserted to DB.'.format(stockname))


if __name__ == "__main__":
    conn = sqlite3.connect('stock.db')
    c = conn.cursor()
    stocknames = ['삼성전자', 'SK하이닉스', 'LG화학', 'LG전자', 'LG이노텍', '삼성에스디에스', '삼성전기', '삼성생명', '삼성화재',
             'SK텔레콤', 'KT', '현대건설', '삼성엔지니어링', '대한항공', '현대차', '기아', '오리온', 'CJ제일제당', '오뚜기',
             '미래에셋대우', '한국금융지주', 'NH투자증권', 'LG생활건강', '아모레퍼시픽', '아모레G', '강원랜드', '호텔신라',
             'KB금융', '신한지주,' '하나금융지주', '롯데쇼핑', '이마트', '신세계', 'GS리테일', 'NAVER', '카카오', 'CJ ENM',
             '스튜디오드래곤', '삼성바이오로직스', '셀트리온', '한미약품', '엔씨소프트', '넷마블', '한화솔루션', 'LS', 'POSCO',
             '고려아연', 'S-Oil', 'SK이노베이션', 'HMM']

    for stockname in stocknames:
        loadData(stockname)
