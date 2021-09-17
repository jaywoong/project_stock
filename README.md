# :chart_with_upwards_trend: 주식 종가 예측 및 포트폴리오 추천:star:

멀티캠퍼스  '빅데이터 기반 지능형 서비스 개발'  과정에서 진행한 파이널 프로젝트입니다.

<img src="https://img.shields.io/static/v1?label=MultiCampus&message=2조&color=olive">	<img src="https://img.shields.io/static/v1?label=Domain&message=Bigdata&color=blueviolet">

<br>

#### **:bulb: 최종 구현**

[YouTube 시연 영상](url첨부)

[결과 보고서]()

---

<br>

### Table of Contents

**1. :mag:[Overview](#idx1)**

**2.  :shamrock:[Process](idx2)**

**2. :book: [Skills](#idx2)**

**3. :dancers: [Team Role](#idx3)**

**4. :clock2: [Project Scheduling](#idx4)**



<br>

## :mag: Overview <a id="idx1"></a> 

- #### **주제**

주식 종가 예측 모델링에 그치지 않고, 예상되는 종가, 리스크, 변동성을 활용하여 고객에게 최적화된 알고리즘을 추천해주는 서비스. 



- #### **데이터 출처**

http://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd

https://kr.investing.com/indices/nasdaq-composite-historical-data



- #### **필요성** 

투자자의 성향을 고려하지 않고 개별종목과 포트폴리오를 추천해 줄 경우  손실을 인내하기 쉽지 않다.  따라서 개별주의 미래 종가를 예측하고,  예상 가격, 변동성, 리스크 등을 고려하여 투자자에게 최적화된 포트폴리오를 구성하는 모델을 구축하고자 한다. 가격예측 모델과 포트폴리오 모델을 활용하여,  고객의 투자 성향 및 보유 종목에 따른 주식 포트폴리오 추천 서비스를 제공하려 한다.



- #### 주요 기능

1. **주식 종가 예측 :seedling: :**
2. **사용자 투자 성향 조사 :eyes: :**
3. **사용자 맞춤 주식 포트폴리오 추천 :gift: :** 



<br>

##  :shamrock: Process <a id= 'idx2'></a>

- #### Service Architecture

  <br>

- #### ERD

  <br>

- #### 요구사항 정의서



<br>

 ## :book: Skills <a id="idx3"></a>

- #### 기술 스택

| Domain    | Name             | Comment         |
| --------- | ---------------- | --------------- |
| Frontend  | HTML             | 페이지 구현     |
| Frontend  | CSS              | 페이지 디자인   |
| Frontend  | JS               |                 |
| Frontend  | Ajax             |                 |
| Backend   | Python           |                 |
| Backend   | SQLite3          | 데이터베이스    |
| Backend   | Django           | 개발 프레임워크 |
| Backend   |                  |                 |
| 개발 환경 | Pycharm          |                 |
| 개발 환경 | Jupyter Notebook |                 |
| 협업      | Github           |                 |
| 협업      | Google Docs      |                 |
| 협업      | Zoom             |                 |
| 배포      | Groom.io         |                 |



- #### 주요 라이브러리

  - Scikit-Learn
  - TensorFlow
  - Keras
  - LSTM
  - FBProphet
  - Word2Vec
  - Pandas
  - Numpy
  - Selenium, Beautifulsoup
  - Matplotlib



- #### 디렉토리 구조





<br>

## :dancers: Team  <a id="idx4"></a>

|       Role       |  Name  |          GitHub           |
| :--------------: | :----: | :-----------------------: |
|        PM        | 이재웅 | https://github.com/jaywoong |
|     Backend     | 서미오 | https://github.com/mmeooo |
| MachineLearning | 송건룡 |                           |
|    Frontend     | 김병현 |                           |
|     Backend     | 유준웅 |                           |



<br>

## :clock2: Project Scheduling <a id="idx5"></a>

```
09/02 ~ 09/04 : 데이터 수집, 웹 스크래핑
08/31 ~ 9/01: 팀 업무분장, 주제 설정

09/00 ~ 09/19 : 종가 예측 모델 구축을 위한 전처리
09/17 ~ 09/18 : 포트폴리오 추천 모델 구축을 위한 전처리

09/00 ~ 09/19 : 웹 서버 구현
09/17 ~ 09/18 : 데이터 시각화

09/30 : ppt 작성
10/01 : 최종발표
```





