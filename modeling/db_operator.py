import schedule
import time
from modeling.stock_db_schedule import UpdateDB

def stock():
    udb = UpdateDB()  # 클래스 선언
    udb.mergeINVEST()  # sp, cboe, exchangerate, nasdaq, futures2y, futures10y
    codes = ['005930', '000660', '051910', '066570', '011070', '018260', '009150', '032830',
            '000810', '017670', '030200', '000720', '028050', '003490', '005380', '000270',
            '271560', '097950', '007310', '006800', '071050', '005940', '051900', '090430',
            '002790', '035250', '008770', '105560', '055550', '086790', '023530', '139480',
            '004170', '007070', '035420', '035720', '035760', '253450', '207940', '068270',
            '128940', '036570', '251270', '009830', '006260', '005490', '010130', '010950',
            '096770', '011200']
    for code in codes:
        udb.getKRX(code)  # y, volume, per, pbr, institution, corp, retail, foreign
        udb.saving()  # db에 최종 저장
    udb.conn.close()


# 스크래핑 및 전처리 실행
schedule.every().day.at("05:32").do(stock)
# schedule.every(1).minutes.do(stock)
while True:
    schedule.run_pending()
    time.sleep(1)