import schedule
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

class Preprocessing:
    def webs():
        driver = webdriver.Chrome('C:\chromedriver.exe')
        driver.get('https://www.bigkinds.or.kr/v2/news/index.do')
        driver.set_window_size(1280,1080)

        driver.find_element_by_xpath('//*[@id="collapse-step-1-body"]/div[3]/div/div[1]/div[1]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="srch-tab1"]/div/div[1]/span[2]').click()

        querytxt = input('크롤링할 키워드는 무엇입니까?:')
        searchbox = driver.find_element_by_id("total-search-key")
        searchbox.send_keys(querytxt)
        searchbox.send_keys("\n")

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="filterTab03"]/li[2]/span').click()

        driver.find_element_by_xpath('//*[@id="select2"]/option[4]').click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        pageNum = soup.select('div.lastNum')
        totalPage = int(pageNum[0]['data-page'])
        totalPage
        ontents = []
        texts=[]
        curPage = 1

        while curPage <= totalPage:
            # bs4 초기화
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            # 기사 리스트
            articles = soup.select('div.news-inner')
            # 페이지 번호 출력
            print('----- Current Page : {}'.format(curPage), '------')

            # 세부 데이터
            for article in articles:
                title = article.select_one('span.title-elipsis').text.strip()
                press =  article.select_one('div.info > div > a').text.strip()
                category = article.select_one('div.info > div > span.bullet-keyword').text.strip()
                date = article.select_one('div.info > p').text.strip()
                contents.append([title, press, category, date])

            # 기사 전문
            for i in range(len(articles)):
                driver.find_elements_by_css_selector('span.title-elipsis')[i].click()
                time.sleep(1)
                text = driver.find_elements_by_css_selector('div.news-view-body')[0].text
                texts.append(text.replace('\n', ''))

                driver.find_element_by_xpath("//div[@id='news-detail-modal']/div/div/button").click()
                time.sleep(1)

            # 페이지 수 증가
            curPage += 1
            if curPage > totalPage:
                print('Crawling succeed')
                break

            # 페이지 이동 클릭
            driver.implicitly_wait(3)
            nextbtn = driver.find_element_by_xpath('//*[@id="news-results-tab"]/div[6]/div[1]/div/div/div/div[4]/a')
            driver.execute_script("arguments[0].click();", nextbtn)

            # bs4 인스턴스 삭제
            del soup
            time.sleep(1.5)

        # 브라우저 종료
        driver.close()

        len(contents)

        df = pd.DataFrame(data=contents, columns =['title', 'press', 'category', 'date'])
        df['text'] = texts
        # 파일 경로 지정
        # df.to_excel("C:/Develops/save/1.xlsx", index=False)
        df.to_excel("C:/Develops/save/" + querytxt +".xlsx", index=False)


    def webn():
        url = 'https://m.stock.naver.com/index.html#/domestic/stock/005930/finance/ESG'
        driver = webdriver.Chrome('C:\chromedriver.exe')
        driver.get(url)

        html= driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        results = soup.select('div.NonFinanceGraph_barDesc__3JwKr')
        len(results)

        results[0], results[1], results[27]

        titles = soup.select('strong.NonFinanceGraph_title__2Ngxx')
        len(titles)

        titles[0], titles[1], titles[13]

        tags = soup.select("li.NonFinanceGraph_item__1iY8U")
        len(tags)

        tags[0]

        title = tags[0].select('strong.NonFinanceGraph_title__2Ngxx')
        title[0].text.strip()

        value = tags[0].select('div.NonFinanceGraph_barDesc__3JwKr').text.strip()
        value[0].text.strip()

        value[1].text.strip()

        contents = []
        for tag in tags:
            title = tag.select('strong.NonFinanceGraph_title__2Ngxx')
            value = tag.select('div.NonFinanceGraph_barDesc__3JwKr')
            contents.append([title[0].text.strip(), value[0].text.strip(), value[1].text.strip()])

        df = pd.DataFrame(contents, columns=['title', 'value', 'average'])
        print(df)

        df.to_excel('C:/Develops/save/삼성전자ESG.xlsx', index= False)






    def job():

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
    

# 매일 실행
schedule.every().day.at("17:17").do(webs)
schedule.every().day.at("17:18").do(job)



while True:
    schedule.run_pending()
    time.sleep(1)