from preprocessing import Preprocessing
from pred_machine import Prediction
from portfolio_model import OptimizePortfolio
from stock_db_schedule import UpdateDB



prep = Preprocessing()
pred = Prediction()
opti = OptimizePortfolio()
ubd = UpdateDB()





opti.merge_predicteions()
opti.pf1(merged_data)
opti.pf2(merged_data)
opti.pf3(merged_data)
opti.pf4(merged_data)
opti.pf5(merged_data)
opti.custom(10000000,55)



pred_machine()
# schedule.every().hour.do(pred_machine)
schedule.every().day.at("6:00").do(pred_machine)

while True:
    schedule.run_pending()
    print(data)
    time.sleep(3600)





# 매일 실행
schedule.every().day.at("17:17").do(webs)
schedule.every().day.at("17:18").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)