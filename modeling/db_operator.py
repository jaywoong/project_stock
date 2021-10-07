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
#schedule.every().day.at("05:32").do(stock)
schedule.every(1).minutes.do(stock)
while True:
    schedule.run_pending()
    time.sleep(1)






# import sqlite3
# # from preprocessing import Preprocessing
# from pred_machine import Prediction
# from portfolio_model import OptimizePortfolio
# from stock_db_schedule import UpdateDB
# import schedule
# import time
#
# # class 선언
# # prep = Preprocessing()
# predic = Prediction()
# opti = OptimizePortfolio()
#
# # 주식 종목 명
# stock_name_list = ['삼성전자', 'SK하이닉스', 'LG화학', 'LG전자', 'LG이노텍', '삼성에스디에스', '삼성전기', '삼성생명', '삼성화재',
#              'SK텔레콤', 'KT', '현대건설', '삼성엔지니어링', '대한항공', '현대차', '기아', '오리온', 'CJ제일제당', '오뚜기',
#              '미래에셋대우', '한국금융지주', 'NH투자증권', 'LG생활건강', '아모레퍼시픽', '아모레G', '강원랜드', '호텔신라',
#              'KB금융', '신한지주,' '하나금융지주', '롯데쇼핑', '이마트', '신세계', 'GS리테일', 'NAVER', '카카오', 'CJENM',
#              '스튜디오드래곤', '삼성바이오로직스', '셀트리온', '한미약품', '엔씨소프트', '넷마블', '한화솔루션', 'LS', 'POSCO',
#              '고려아연', 'S-Oil', 'SK이노베이션', 'HMM']
#
# # 데이터 업데이트
# def udbstock():
#     udb = UpdateDB()
#     udb.mergeINVEST()  # sp, cboe, exchangerate, nasdaq, futures2y, futures10y
#     codes = ['005930', '000660', '051910', '066570', '011070', '018260', '009150', '032830',
#             '000810', '017670', '030200', '000720', '028050', '003490', '005380', '000270',
#             '271560', '097950', '007310', '006800', '071050', '005940', '051900', '090430',
#             '002790', '035250', '008770', '105560', '055550', '086790', '023530', '139480',
#             '004170', '007070', '035420', '035720', '035760', '253450', '207940', '068270',
#             '128940', '036570', '251270', '009830', '006260', '005490', '010130', '010950',
#             '096770', '011200']
#     for code in codes:
#         udb.getKRX(code)  # y, volume, per, pbr, institution, corp, retail, foreign
#         udb.saving()
#     udb.conn.close()
#
# # 스크래핑 및 전처리 실행
# schedule.every().day.at("05:10").do(udbstock)
#
# # 주가 예측 모델 실행
# schedule.every().day.at("05:20").do(predic.pred_machine(stock_name_list))
#
# # 포트폴리오 모델 실행
# # schedule.every().day.at("06:20").do(opti.merge_predictions(stock_name_list))
# schedule.every().day.at("07:25").do(opti.pf1(merged_data))
# schedule.every().day.at("07:26").do(opti.pf2(merged_data))
# schedule.every().day.at("07:27").do(opti.pf3(merged_data))
# schedule.every().day.at("07:28").do(opti.pf4(merged_data))
# schedule.every().day.at("07:29").do(opti.pf5(merged_data))
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)


