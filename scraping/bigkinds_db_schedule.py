import sqlite3
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

class Bigkinds:
    def __init__(self):
        self.options = Options()
        # headless는 화면이나 페이지 이동을 표시하지 않고 동작하는 모드 (브라우저 창 안보이기)
        self.options.add_argument('headless')
        self.driver = webdriver.Chrome('C:\chromedriver.exe', options=self.options)

    def getURL(self,url):
        # 빅카인즈 사이트 이동
        self.driver.implicitly_wait(2)
        self.driver.set_window_size(1300, 700)
        self.driver.get(url)
        # 검색기간 설정
        self.driver.find_element_by_xpath('//*[@id="collapse-step-1-body"]/div[3]/div/div[1]/div[1]/a').click()
        time.sleep(3)
        # 1일
        self.driver.find_element_by_xpath('//*[@id="srch-tab1"]/div/div[1]/span[1]/label').click()
        # 1주일
        # self.driver.find_element_by_xpath('//*[@id="srch-tab1"]/div/div[1]/span[2]/label').click()
        time.sleep(3)

    def getPage(self, url, querytxt):
        self.getURL(url)
        # 검색어 입력
        searchbox = self.driver.find_element_by_id("total-search-key")
        searchbox.send_keys(querytxt)
        searchbox.send_keys("\n")  # 검색버튼 엔터
        time.sleep(2)
        # 기사 분류 -> 경제로 설정
        self.driver.find_element_by_xpath('//*[@id="filterTab03"]/li[2]/span').click()
        time.sleep(3)
        # 기사 100건 씩 출력
        self.driver.find_element_by_xpath('//*[@id="select2"]/option[4]').click()
        time.sleep(3)
        # 전체 페이지 개수
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        pageNum = soup.select('div.lastNum')[0].text
        self.totalPage  = int(pageNum)
        del soup

    def crawling(self, url, stockname):
        self.getPage(url, stockname)
        print('{} crawling start.'.format(stockname))
        print('Total Pages : ', self.totalPage)
        curPage = 1  # 현재 페이지
        self.contents = []
        self.texts = []
        while curPage <= self.totalPage:
            # bs4 초기화
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            # 기사 리스트
            articles = soup.select('div.news-inner')
            # 페이지 번호 출력
            print('Current Page : {}'.format(curPage))
            # 세부 데이터
            for article in articles:
                title = article.select_one('span.title-elipsis').text.strip()
                try:
                    press = article.select_one('div.info > div > a.provider').text.strip()
                    category = article.select_one('div.info > div > span.bullet-keyword').text.strip()
                    date = article.select_one('div.info > p.name').text.strip()
                except:
                    press = None
                    pass

                if press != None:
                    self.contents.append([title, press, category, date])
                time.sleep(3)
            # 기사 전문
            for i in range(len(articles)):
                self.driver.find_elements_by_css_selector('span.title-elipsis')[i].click()
                time.sleep(4)
                text = self.driver.find_elements_by_css_selector('div.news-view-body')[0].text
                self.texts.append(text.replace('\n', ''))
                self.driver.find_element_by_xpath("//div[@id='news-detail-modal']/div/div/button").click()
                time.sleep(4)

            # 페이지 수 증가
            curPage += 1
            if curPage > self.totalPage:
                print('{} crawling succeed.'.format(stockname))
                break
            # 페이지 이동 클릭
            self.driver.implicitly_wait(3)
            try:
                nextbtn = self.driver.find_element_by_xpath('//*[@id="news-results-tab"]/div[1]/div[2]/div/div/div/div/div[4]/a')
            except:
                nextbtn = self.driver.find_element_by_xpath('//*[@id="news-results-tab"]/div[6]/div[2]/div/div/div/div/div[4]/a')
            self.driver.execute_script("arguments[0].click();", nextbtn)
            # bs4 인스턴스 삭제
            del soup
            time.sleep(3)

    def saving(self, stockname):
        # 브라우저 종료
        self.driver.close()
        self.df_news = pd.DataFrame(data=self.contents, columns =['title', 'press', 'category', 'date'])
        self.df_news['text'] = self.texts
        self.df_news.to_sql('{}_news'.format(stockname), conn, if_exists='append', index=False)  # 테이블명
        conn.commit()
        print('{} inserted to DB.'.format(stockname))



if __name__ == "__main__":
    conn = sqlite3.connect('bigkinds.db')
    c = conn.cursor()

    def crawl():
        url = 'https://www.bigkinds.or.kr/v2/news/index.do'
        stocknames = ['삼성전자', 'SK하이닉스', 'LG화학', 'LG전자', 'LG이노텍', '삼성에스디에스', '삼성전기', '삼성생명', '삼성화재',
             'SK텔레콤', 'KT', '현대건설', '삼성엔지니어링', '대한항공', '현대차', '기아', '오리온', 'CJ제일제당', '오뚜기',
             '미래에셋증권', '한국금융지주', 'NH투자증권', 'LG생활건강', '아모레퍼시픽', '아모레G', '강원랜드', '호텔신라',
             'KB금융', '신한지주,' '하나금융지주', '롯데쇼핑', '이마트', '신세계', 'GS리테일', 'NAVER', '카카오', 'CJ ENM',
             '스튜디오드래곤', '삼성바이오로직스', '셀트리온', '한미약품', '엔씨소프트', '넷마블', '한화솔루션', 'LS', 'POSCO',
             '고려아연', 'S-Oil', 'SK이노베이션', 'HMM']
        for stockname in stocknames:
            crawl = Bigkinds()
            crawl.crawling(url, stockname)
            crawl.saving(stockname)
        conn.close()

    schedule.every().day.at("5:30").do(crawl)  # 매일 5:30에 동작
    # schedule.every().monday.at("5:30").do(crawl)  # 매주 월요일 5:30에 동작
    while True:
        schedule.run_pending()
        time.sleep(1)
