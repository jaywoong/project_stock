from django.shortcuts import render, redirect
import sqlite3


def index(request):
    return render(request, 'index.html')
def main(request):
    return render(request, 'main.html')
def getdata(request):
    return render(request, 'getdata.html')
def team(request):
    return render(request, 'team.html')
def news_amore(request):
    return render(request, 'amore.html')
def news_hanmi(request):
    return render(request, 'hanmi.html')
def news_hmm(request):
    return render(request, 'hmm.html')
def news_lg(request):
    return render(request, 'lg.html')
def news_nh(request):
    return render(request, 'nh.html')
def news_orion(request):
    return render(request, 'orion.html')
def news(request):
    return render(request, 'news.html')
def portpolio(request):
    return render(request, 'portpolio.html')
def mgetdata(request):
    return render(request, 'mgetdata.html')

# def inner(request):
#     return render(request, 'inner-page.html')


def news_amore(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('아모레퍼시픽'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('아모레퍼시픽'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'amore.html', result)

def news_hanmi(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('한미약품'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('한미약품'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'hanmi.html', result)

def news_hmm(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('hmm'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('hmm'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'hmm.html', result)

def news_lg(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('LG생활건강'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('LG생활건강'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'lg.html', result)

def news_nh(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('NH투자증권'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('NH투자증권'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'nh.html', result)

def news_orion(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('오리온'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('오리온'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'orion.html', result)
