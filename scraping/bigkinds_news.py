import sqlite3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time


class Bigkinds:
    def __init__(self):
        self.options = Options()
        # headless는 화면이나 페이지 이동을 표시하지 않고 동작하는 모드 (브라우저 창 안보이기)
        #self.options.add_argument('headless')
        self.driver = webdriver.Chrome('C:\chromedriver.exe', options=self.options)

    def getURL(self,url):
        # 빅카인즈 사이트 이동
        self.driver.implicitly_wait(2)
        self.driver.set_window_size(1300,800)
        self.driver.get(url)
        # 검색기간 1주일로 설정
        self.driver.find_element_by_xpath('//*[@id="collapse-step-1-body"]/div[3]/div/div[1]/div[1]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="srch-tab1"]/div/div[1]/span[2]').click()
        time.sleep(2)

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

    def crawling(self, url, querytxt):
        self.getPage(url, querytxt)
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
                press =  article.select_one('div.info > div > a.provider').text.strip()
                category = article.select_one('div.info > div > span.bullet-keyword').text.strip()
                date = article.select_one('div.info > p.name').text.strip()
                self.contents.append([title, press, category, date])
            # 기사 전문
            for i in range(len(articles)):
                self.driver.find_elements_by_css_selector('span.title-elipsis')[i].click()
                time.sleep(2)
                text = self.driver.find_elements_by_css_selector('div.news-view-body')[0].text
                self.texts.append(text.replace('\n', ''))
                self.driver.find_element_by_xpath("//div[@id='news-detail-modal']/div/div/button").click()
                time.sleep(1)
            # 페이지 수 증가
            curPage += 1
            if curPage > self.totalPage:
                print('Crawling succeed')
                break
            # 페이지 이동 클릭
            self.driver.implicitly_wait(3)
            nextbtn = self.driver.find_element_by_xpath('//*[@id="news-results-tab"]/div[6]/div[1]/div/div/div/div[4]/a')
            self.driver.execute_script("arguments[0].click();", nextbtn)
            # bs4 인스턴스 삭제
            del soup
            time.sleep(2)

    def saving(self, querytxt):
        # 브라우저 종료
        self.driver.close()
        self.df_news = pd.DataFrame(data=self.contents, columns =['title', 'press', 'category', 'date'])
        self.df_news['text'] = self.texts
        self.df_news.to_sql('{}_news'.format(querytxt), conn, if_exists='append', index=False)  # 테이블명
        conn.commit()
        conn.close()


if __name__ == "__main__":
    conn = sqlite3.connect('bigkinds.db')
    c = conn.cursor()

    url = 'https://www.bigkinds.or.kr/v2/news/index.do'
    querytxt = '오리온'
    crawl = Bigkinds()
    crawl.crawling(url, querytxt)
    crawl.saving(querytxt)
