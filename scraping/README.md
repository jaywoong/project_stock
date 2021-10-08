### 디렉토리 구조

```
📦scraping
 ┣ 📂notebook
 ┃ ┣ 📜bigkinds.ipynb
 ┃ ┣ 📜bigkinds_db_analog.ipynb
 ┃ ┣ 📜investingcom.ipynb
 ┃ ┣ 📜krx.ipynb
 ┃ ┗ 📜naverESG.ipynb
 ┣ 📜bigkinds.db
 ┗ 📜bigkinds_db_schedule.py
```



### 데이터 수집

- 데이터 수집 대상

  `삼성전자, SK하이닉스, LG화학, LG전자, LG이노텍, 삼성에스디에스, 삼성전기, 삼성생명, 삼성화재, SK텔레콤, KT, 현대건설, 삼성엔지니어링, 대한항공, 현대차, 기아, 오리온, CJ제일제당, 오뚜기, 미래에셋대우, 한국금융지주, NH투자증권, LG생활건강, 아모레퍼시픽, 아모레G, 강원랜드, 호텔신라, KB금융, 신한지주, 하나금융지주, 롯데쇼핑, 이마트, 신세계, GS리테일, NAVER, 카카오, CJENM, 스튜디오드래곤, 삼성바이오로직스, 셀트리온, 한미약품, 엔씨소프트, 넷마블, 한화솔루션, LS, POSCO,고려아연, S-Oil, SK이노베이션, HMM`

  

- 데이터 출처 및 수집 방법

  - 공통 거시 경제 지표 중 `S&P, CBOE` 는 `DataFinanceReader` 모듈을 통해 수집하고,

    `NASDAQ, futures2y, futures10y` 은 [인베스팅닷컴](https://kr.investing.com/indices/nasdaq-composite-historical-data)  스크래핑을 통해 수집했습니다.

  - 개별주 관련 지표인 `거래량, atr, PER, PBR, 기관합계, 기타법인, 개인, 외국인합계` 는 [KRX](http://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd) 데이터를 제공하는 `pykrx` 모듈을 통해 수집했습니다. 

  - [빅카인즈](https://www.bigkinds.or.kr/) 에서 기업별 최근 일주일 뉴스기사를 스크래핑하여 수집해 웹에서 제공했습니다.

  ```
  # scraping/bigkinds_db_schedule.py
  
  from selenium import webdriver
  from bs4 import BeautifulSoup
  class Bigkinds:
      def __init__(self):
          self.driver = webdriver.Chrome('C:\chromedriver.exe')
      def crawling(self, url, stockname):
       	while curPage <= self.totalPage:
              soup = BeautifulSoup(self.driver.page_source, 'html.parser')
              articles = soup.select('div.news-inner')
              print('Current Page : {}'.format(curPage))
              for article in articles:
                  title = article.select_one('span.title-elipsis').text.strip()
                  press = article.select_one('div.info > div > a.provider').text.strip()
                  category = article.select_one('div.info > div > span.bullet-keyword').text.strip()
                   date = article.select_one('div.info > p.name').text.strip()
                   self.contents.append([title, press, category, date])
   
  ```

  

  

### SQLite3 연동

```
# 수집한 데이터를 DataFrame으로 합쳐 sqlite3에 저장하였습니다.
# modeling/stock_db_schedule.py

import sqlite3
class UpdateDB:
    def __init__(self):
        self.conn = sqlite3.connect('../modeling/stock.db')
        self.c = self.conn.cursor()  
        
   def saving(self):  
        self.df_merge = pd.merge(self.df_krx, self.df_invest, on='date')
        self.df_merge.to_sql('{}'.format(self.stockname), self.conn, 	if_exists='append')  
        self.conn.commit()

```

```
# 저장된 sqlite3를 웹에서 호출하였습니다.
# stock/views.py

def news(request):
	result = dict()
	db_news = sqlite3.connect('bigkinds.db')
	db_news.row_factory = sqlite3.Row
	c = db_news.cursor()
	c.execute("select title, press, category, date, text from {}_news".format('CJENM'))
    data = c.fetchall()
    result['erows'] = data
    
    return render(request, 'news.html', result)
```
