# ChickenStock :chicken:

### :chart_with_upwards_trend: 주식 종가 예측 및 포트폴리오 추천 :star:

> 멀티캠퍼스  '빅데이터 기반 지능형 서비스 개발'  과정에서 진행한 파이널 프로젝트입니다.
>
> 참여 :  [jaywoong](https://github.com/jaywoong),  [mmeooo](https://github.com/mmeooo),  [00FFEF](https://github.com/00FFEF),  [top430](https://github.com/top430),  [yoojunwoong](https://github.com/yoojunwoong)

<img src="https://img.shields.io/static/v1?label=MultiCampus&message=Team2&color=yellow">	<img src="https://img.shields.io/static/v1?label=Domain&message=Bigdata&color=green">

#### **:bulb: 최종 구현**

**[YouTube시연](https://youtu.be/m00NjTMoaJs)** &nbsp;&nbsp; **[결과 보고서](md-images/chickenstock.pdf)**

####  **Table of Contents**

**:mag:[Overview](#idx1)** **:shamrock:[Process](#idx2)** **:book: [Skills](#idx2)** **:dancers: [Team](#idx3)** **:clock2: [Scheduling](#idx4)**

___



## :mag: Overview <a id="idx1"></a>

- #### **주제**

주식 종가 예측 모델링에 그치지 않고, 포트폴리오 모델을  활용하여 투자자의 투자 성향에 따른 주식 포트폴리오를 추천해주는 서비스 

- #### **필요성** 

투자자의 성향을 고려하지 않고 개별 종목과 포트폴리오를 추천해 줄 경우  손실을 인내하기 쉽지 않다.  따라서 개별주의 종가를 예측하고,  예상 가격, 변동성, 리스크 등을 고려하여 투자자에게 최적화된 포트폴리오를 구성하는 모델을 구축하고자 한다. 가격예측 모델과 포트폴리오 모델을 활용하여,  고객의 투자 성향 및 위험 감내 수준에 따른 주식 포트폴리오 추천 서비스를 제공하려 한다.

- #### **데이터**

https://kr.investing.com/indices/nasdaq-composite-historical-data

http://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd

- #### 주요 기능

1. **사용자 투자 성향 조사 :eyes:**
2. **주식 종가 예측 :seedling:**
3. **주식 포트폴리오 추천 :gift:**
4. **추천 기업 최근 일주일 뉴스기사 제공 :newspaper:** 

<br>

##  :shamrock: Process <a id= 'idx2'></a>

- #### MVT pattern

  ![프로세스](md-images/%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4.PNG)

- #### ERD

  ![ERD](md-images/ERD.png)

* #### 요구사항 정의서

  ![요구사항정의서](md-images/%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD%EC%A0%95%EC%9D%98%EC%84%9C.PNG)

* #### 화면 정의서

  | ![화면정의서2](md-images/%ED%99%94%EB%A9%B4%EC%A0%95%EC%9D%98%EC%84%9C2.PNG) | ![화면정의서](md-images/%ED%99%94%EB%A9%B4%EC%A0%95%EC%9D%98%EC%84%9C.PNG) |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |

<br>

 ## :book: Skills <a id="idx3"></a>

- #### 기술 스택

  ![환경](md-images/%ED%99%98%EA%B2%BD.PNG)

- #### 디렉토리 구조

  * **Frontend  -  [보러가기](stock/README.md) :heavy_check_mark:**
  * **Backend**
    * **Machine Learning  -  [보러가기](modeling/README.md) :heavy_check_mark:**
    * **Scraping  -  [보러가기](scraping/README.md) :heavy_check_mark:**
  
  <br>

## :dancers: Team <a id="idx4"></a>

![팀](md-images/%ED%8C%80.PNG)

<br>

## :clock2: Scheduling <a id="idx5"></a>

![일정](md-images/%EC%9D%BC%EC%A0%95.PNG)



* #### WBS

![WBS](md-images/WBS.PNG)
