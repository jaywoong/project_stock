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
def news(request):
    return render(request, 'news.html')
# def inner(request):
#     return render(request, 'inner-page.html')

# def newsdata(request):
#     category = request.GET['category'];
#     date = request.GET['date'];
#     press = request.GET['press'];
#     text = request.GET['text'];
#     title = request.GET['title'];
#     return render(request, 'news.html');

def newsdata(request):
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

    return render(request, 'news.html', result)