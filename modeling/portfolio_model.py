import sqlite3
import pandas as pd
import numpy as np
import scipy.optimize as sco

class OptimizePortfolio:
    def merge_predicteions(self):
        global merged_data
        merged_data = pd.DataFrame({'samsung1':[1,1,1,2,3,4],'lg1':[1,5,6,6,7,7], 'sk1': [1,2,8,12,10,11], 'ls1': [1,13,18,16,20,15],
                             'samsung2':[1,1,1,2,3,4],'lg2':[1,5,6,6,7,17], 'sk2': [1,2,8,12,13,11], 'ls2': [1,13,18,8,12,10],
                             'samsung3':[1,1,1,2,3,4],'lg3':[1,5,6,16,7,7], 'sk3': [1,2,8,12,16,11], 'ls3': [1,13,18,12,10,20],
                             'samsung4':[1,1,1,2,3,4],'lg4':[1,5,6,6,17,7], 'sk4': [1,2,8,12,10,11], 'ls4': [1,13,18,11,20,23],
                             'samsung5':[1,1,1,2,3,4],'lg5':[1,5,6,6,7,20], 'sk5': [1,2,8,12,12,11], 'ls5': [1,18,12,10,20,25],
                             'samsung6':[1,1,1,2,3,4],'lg6':[1,5,3,6,7,7], 'sk6': [1,2,8,12,17,11], 'ls6': [1,13,1,6,20,18],
                             'samsung7':[1,1,1,2,3,4],'lg7':[1,5,6,6,7,8], 'sk7': [1,2,8,12,18,11], 'ls7': [1,1,8,16,20,15],
                             'samsung8':[1,1,1,2,3,4],'lg8':[1,5,3,6,7,7]})
        return


    def pf1(self, merged_data):
        global pf1
        rets = np.log(merged_data / merged_data.shift(1))
        rets = rets.drop(0)
        top25 = rets.mean().sort_values(ascending = False).head(25)
        rets = rets[top25.index]
        covmat = rets.cov()*10

        def minvar(weights):
            return np.sqrt(weights.T @ covmat @ weights)

        w = np.array([0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04])
        cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x) - 1})                     # 합계가 1이 되도록
        bnds = ((0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1),(0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1),(0,1), (0,1), (0,1), (0,1), (0,1))

        opt = sco.minimize(minvar, w, method='SLSQP', bounds=bnds, constraints=cons)

        buy = opt['x']>0.05
        pf1 = pd.DataFrame({'stock' : top25.index[buy], 'ratio': np.round(opt['x'][buy],2)})

        return


    def pf2(self, merged_data):
        global pf2
        rets = np.log(merged_data / merged_data.shift(1))
        rets = rets.drop(0)
        top20 = rets.mean().sort_values(ascending = False).head(20)
        rets = rets[top20.index]
        covmat = rets.cov()*10

        def minvar(weights):
            return np.sqrt(weights.T @ covmat @ weights)

        w = np.array([0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05])
        cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x) - 1})                     # 합계가 1이 되도록
        bnds = ((0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1))

        opt = sco.minimize(minvar, w, method='SLSQP', bounds=bnds, constraints=cons)

        buy = opt['x']>0.05
        pf2 = pd.DataFrame({'stock' : top20.index[buy], 'ratio': np.round(opt['x'][buy],2)})

        return


    def pf3(self, merged_data):
        global pf3
        rets = np.log(merged_data / merged_data.shift(1))
        rets = rets.drop(0)
        top15 = rets.mean().sort_values(ascending = False).head(15)
        rets = rets[top15.index]
        covmat = rets.cov()*10

        def minvar(weights):
            return np.sqrt(weights.T @ covmat @ weights)

        w15 = 1/15
        w = np.array([w15,w15,w15,w15,w15,w15,w15,w15,w15,w15,w15,w15,w15,w15,w15])
        cons = ({'type': 'eq', 'fun': lambda x:  np.sum(x) - 1})                     # 합계가 1이 되도록
        bnds = ((0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1), (0,1))

        opt = sco.minimize(minvar, w, method='SLSQP', bounds=bnds, constraints=cons)

        buy = opt['x']>0.05
        pf3 = pd.DataFrame({'stock' : top15.index[buy], 'ratio': np.round(opt['x'][buy],2)})

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
        pf4 = pd.DataFrame({'stock' : top10.index[buy], 'ratio': np.round(opt['x'][buy],2)})

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
        pf5 = pd.DataFrame({'stock' : top5.index[buy], 'ratio': np.round(opt['x'][buy],2)})

        return


    def custom(self, total_asset, risk_score):  # 설문에서 total_asset 500만원 이상 정수로 받기
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

            # conn = sqlite3.connect('./' + stock_name + '.db')
            # c = conn.cursor()
            # stock_data = pd.read_sql('SELECT * FROM ' + stock_name, con=conn)
            # c.close()

# ---------------------------------------------------------------------------------------------------------------------------
            stock_data = pd.DataFrame({'samsung1':[1,1,1,2,3,4],'lg1':[1,5,6,6,7,7], 'sk1': [1,2,8,12,10,11], 'ls1': [1,13,18,16,20,15],
                                       'samsung2':[1,1,1,2,3,4],'lg2':[1,5,6,6,7,17], 'sk2': [1,2,8,12,13,11], 'ls2': [1,13,18,8,12,10],
                                       'samsung3':[1,1,1,2,3,4],'lg3':[1,5,6,16,7,7], 'sk3': [1,2,8,12,16,11], 'ls3': [1,13,18,12,10,20],
                                       'samsung4':[1,1,1,2,3,4],'lg4':[1,5,6,6,17,7], 'sk4': [1,2,8,12,10,11], 'ls4': [1,13,18,11,20,23],
                                       'samsung5':[1,1,1,2,3,4],'lg5':[1,5,6,6,7,20], 'sk5': [1,2,8,12,12,11], 'ls5': [1,18,12,10,20,25],
                                       'samsung6':[1,1,1,2,3,4],'lg6':[1,5,3,6,7,7], 'sk6': [1,2,8,12,17,11], 'ls6': [1,13,1,6,20,18],
                                       'samsung7':[1,1,1,2,3,4],'lg7':[1,5,6,6,7,8], 'sk7': [1,2,8,12,18,11], 'ls7': [1,1,8,16,20,15],
                                       'samsung8':[1,1,1,2,3,4],'lg8':[1,5,3,6,7,73500]})
# ---------------------------------------------------------------------------------------------------------------------------

            stock_price = stock_data.iloc[-1,-1]
            stock_buy = total_asset * pf_num.iloc[i,1]
            num_of_shares = int(stock_buy/stock_price)
            amount = num_of_shares*stock_price

            custom_pf = custom_pf.append({'stock_name' : stock_name , 'num_of_shares' : num_of_shares, 'amount' : amount, 'ratio' : pf1.iloc[i,1]} , ignore_index=True)

        return print(custom_pf)


op = OptimizePortfolio()
op.merge_predicteions()
op.pf1(merged_data)
op.pf2(merged_data)
op.pf3(merged_data)
op.pf4(merged_data)
op.pf5(merged_data)
op.custom(1000000,55)
