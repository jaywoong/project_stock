import sqlite3
import pandas as pd
import numpy as np
import scipy.optimize as sco

class OptimizePortfolio:
    def merge_predictions(self, stock_name_list):
        global merged_data

        for stock_name in stock_name_list:
            merged_data[stock_name] = stock_name.iloc[-11:,-1]
        return

    def pf1(self, merged_data):
        global pf1
        rets = np.log(merged_data / merged_data.shift(1))
        rets = rets.drop(0)
        top40 = rets.mean().sort_values(ascending = False).head(40)
        rets = rets[top40.index]
        covmat = rets.cov()*10

        def minvar(weights):
            return np.sqrt(weights.T @ covmat @ weights)

        w40 = 1/40
        w = np.array([w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,w40,])
        cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x) - 1})
        bnds = ((0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1),(0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1),(0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1),(0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1))

        opt = sco.minimize(minvar, w, method='SLSQP', bounds=bnds, constraints=cons)

        buy = opt['x'] > 0.05
        pf1 = pd.DataFrame({'stock' : top40.index[buy], 'ratio': np.round(opt['x'][buy],3)})

        return


    def pf2(self, merged_data):
        global pf2
        rets = np.log(merged_data / merged_data.shift(1))
        rets = rets.drop(0)
        top30 = rets.mean().sort_values(ascending = False).head(30)
        rets = rets[top30.index]
        covmat = rets.cov()*10

        def minvar(weights):
            return np.sqrt(weights.T @ covmat @ weights)

        w30 = 1/30
        w = np.array([w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30,w30])
        cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x) - 1})
        bnds = ((0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1))

        opt = sco.minimize(minvar, w, method='SLSQP', bounds=bnds, constraints=cons)

        buy = opt['x']>0.05
        pf2 = pd.DataFrame({'stock' : top30.index[buy], 'ratio': np.round(opt['x'][buy],3)})

        return


    def pf3(self, merged_data):
        global pf3
        rets = np.log(merged_data / merged_data.shift(1))
        rets = rets.drop(0)
        top20 = rets.mean().sort_values(ascending = False).head(20)
        rets = rets[top20.index]
        covmat = rets.cov()*10

        def minvar(weights):
            return np.sqrt(weights.T @ covmat @ weights)

        w = np.array([0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05])
        cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x) - 1})
        bnds = ((0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1))

        opt = sco.minimize(minvar, w, method='SLSQP', bounds=bnds, constraints=cons)

        buy = opt['x']>0.05
        pf3 = pd.DataFrame({'stock' : top20.index[buy], 'ratio': np.round(opt['x'][buy],3)})

        return


    def pf4(self, merged_data):
        global pf4
        rets = np.log(merged_data / merged_data.shift(1))
        rets = rets.drop(0)
        top10 = rets.mean().sort_values(ascending = False).head(10)
        rets = rets[top10.index]
        covmat = rets.cov()*10

        def minvar(weights):
            return np.sqrt(weights.T @ covmat @ weights)

        w = np.array([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
        cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x) - 1})                     # 합계가 1이 되도록
        bnds = ((0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1))

        opt = sco.minimize(minvar, w, method='SLSQP', bounds=bnds, constraints=cons)

        buy = opt['x']>0.05
        pf4 = pd.DataFrame({'stock' : top10.index[buy], 'ratio': np.round(opt['x'][buy],3)})

        return


    def pf5(self, merged_data):
        global pf5
        rets = np.log(merged_data / merged_data.shift(1))
        rets = rets.drop(0)
        top5 = rets.mean().sort_values(ascending = False).head(5)
        rets = rets[top5.index]
        covmat = rets.cov()*10

        def minvar(weights):
            return np.sqrt(weights.T @ covmat @ weights)

        w = np.array([0.2,0.2,0.2,0.2,0.2])
        cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x) - 1})                     # 합계가 1이 되도록
        bnds = ((0,1), (0,1), (0,1), (0,1), (0,1))

        opt = sco.minimize(minvar, w, method='SLSQP', bounds=bnds, constraints=cons)

        buy = opt['x']>0.05
        pf5 = pd.DataFrame({'stock' : top5.index[buy], 'ratio': np.round(opt['x'][buy],3)})

        return


    def custom(self, total_asset, risk_score):
        global custom_pf

        if risk_score <= 20:
            pf_num = pf1
        elif risk_score <= 40:
            pf_num = pf2
        elif risk_score <= 60:
            pf_num = pf3
        elif risk_score <= 80:
            pf_num = pf4
        else:
            pf_num = pf5

        custom_pf = pd.DataFrame(columns=['stock_name', 'num_of_shares', 'amount', 'ratio'])

        for i in range(0,len(pf_num)):
            stock_name = pf_num.iloc[i,0]

            conn = sqlite3.connect('./stock.db')
            c = conn.cursor()
            stock_data = pd.read_sql('SELECT * FROM ' + stock_name, con=conn)
            c.close()

            stock_price = stock_data.iloc[-1,-1]
            stock_buy = total_asset * pf_num.iloc[i,1]
            num_of_shares = int(stock_buy/stock_price)
            amount = num_of_shares*stock_price

            custom_pf = custom_pf.append({'stock_name' : stock_name , 'num_of_shares' : num_of_shares, 'amount' : amount, 'ratio' : pf_num.iloc[i,1]} , ignore_index=True)

        return


# op = OptimizePortfolio()
# op.merge_predicteions()
# op.pf1(merged_data)
# op.pf2(merged_data)
# op.pf3(merged_data)
# op.pf4(merged_data)
# op.pf5(merged_data)
# op.custom(10000000,55)
# opti.custom(total_asset, risk_score)
