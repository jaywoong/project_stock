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
def news_amoreg(request):
    return render(request, 'amoreg.html')
def news_celltrion(request):
    return render(request, 'celltrion.html')
def news_cj(request):
    return render(request, 'cj.html')
def news_CJENM(request):
    return render(request, 'CJENM.html')
def news_daehan(request):
    return render(request, 'daehan.html')
def news_emart(request):
    return render(request, 'emart.html')
def news_goryeo(request):
    return render(request, 'goryeo.html')
def news_gs(request):
    return render(request, 'gs.html')
def news_hana(request):
    return render(request, 'hana.html')
def news_hanguk(request):
    return render(request, 'hanguk.html')
def news_hyundae(request):
    return render(request, 'hyundae.html')
def news_hanwha(request):
    return render(request, 'hanwha.html.html')
def news_hyundaebuild(request):
    return render(request, 'hyundaebuild.html')
def news_kakao(request):
    return render(request, 'kakao.html')
def news_kangwon(request):
    return render(request, 'kangwon.html')
def news_kb(request):
    return render(request, 'kb.html')
def news_kia(request):
    return render(request, 'kia.html')
def news_kt(request):
    return render(request, 'kt.html')
def news_lg2(request):
    return render(request, 'lg2.html')
def news_lg3(request):
    return render(request, 'lg3.html')
def news_lg4(request):
    return render(request, 'lg4.html')
def news_lotte(request):
    return render(request, 'lotte.html')
def news_ls(request):
    return render(request, 'ls.html')
def news_mirae(request):
    return render(request, 'mirae.html')
def news_naver(request):
    return render(request, 'naver.html')
def news_ncsoft(request):
    return render(request, 'ncsoft.html')
def news_netmarble(request):
    return render(request, 'netmarble.html')
def news_ottugi(request):
    return render(request, 'ottugi.html')
def news_posco(request):
    return render(request, 'posco.html')
def news_samsung(request):
    return render(request, 'samsung.html')
def news_samsungbio(request):
    return render(request, 'samsungbio.html')
def news_samsungelectronic(request):
    return render(request, 'samsungelectronic.html')
def news_samsungengine(request):
    return render(request, 'samsungengine.html')
def news_samsungfire(request):
    return render(request, 'samsungfire.html')
def news_samsunglife(request):
    return render(request, 'samsunglife.html')
def news_samsungsds(request):
    return render(request, 'samsungsds.html')
def news_shillahotel(request):
    return render(request, 'shillahotel.html')
def shinhan(request):
    return render(request, 'shinhan.html')
def news_shinsegae(request):
    return render(request, 'shinsegae.html')
def news_sk(request):
    return render(request, 'sk.html')
def news_skh(request):
    return render(request, 'skh.html')
def news_skt(request):
    return render(request, 'skt.html')
def news_soil(request):
    return render(request, 'soil.html')
def news_studio(request):
    return render(request, 'studio.html')



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

def news_CJENM(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('CJENM'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('CJENM'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'CJENM.html', result)

def news_cj(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('CJ제일제당'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('CJ제일제당'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'cj.html', result)

def news_gs(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('GS리테일'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('GS리테일'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'gs.html', result)

def news_kb(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('KB금융지주'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('KB금융지주'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'kb.html', result)

def news_kt(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('KT'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('KT'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'kt.html', result)

def news_lg2(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('LG이노텍'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('LG이노텍'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'lg2.html', result)

def news_lg3(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('LG전자'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('LG전자'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'lg3.html', result)

def news_lg4(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('LG화학'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('LG화학'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'lg4.html', result)

def news_ls(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('LS'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('LS'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'ls.html', result)

def news_naver(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('NAVER'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('NAVER'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'naver.html', result)

def news_posco(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('POSCO'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('POSCO'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'posco.html', result)

def news_soil(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('S-Oil'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('S-Oil'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'soil.html', result)

def news_sk(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('SK이노베이션'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('SK이노베이션'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'sk.html', result)

def news_skt(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('SK텔레콤'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('SK텔레콤'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'sk.html', result)

def news_skh(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('SK하이닉스'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('SK하이닉스'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'skh.html', result)

def news_kangwon(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('강원랜드'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('강원랜드'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'kangwon.html', result)

def news_goryeo(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('고려아연'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('고려아연'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'goryeo.html', result)

def news_kia(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('기아'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('기아'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'kia.html', result)

def news_netmarble(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('넷마블'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('넷마블'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'netmarble.html', result)

def news_daehan(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('대한항공'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('대한항공'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'daehan.html', result)

def news_lotte(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('롯데쇼핑'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('롯데쇼핑'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'lotte.html', result)

def news_mirae(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('미래에셋대우'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('미래에셋대우'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'mirae.html', result)

def news_samsungbio(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('삼성바이오로직스'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('삼성바이오로직스'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'samsungbio.html', result)

def news_samsunglife(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('삼성생명'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('삼성생명'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'samsunglife.html', result)

def news_samsungsds(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('삼성에스디에스'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('삼성에스디에스'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'samsungsds.html', result)

def news_samsungengine(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('삼성엔지니어링'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('삼성엔지니어링'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'samsungengine.html', result)

def news_samsungelectronic(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('삼성전기'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('삼성전기'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'samsungelectronic.html', result)

def news_samsung(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('삼성전자'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('삼성전자'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'samsung.html', result)

def news_samsungfire(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('삼성화재'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('삼성화재'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'samsungfire.html', result)

def news_celltrion(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('셀트리온'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('셀트리온'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'celltrion.html', result)

def news_studio(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('스튜디오드래곤'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('스튜디오드래곤'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'studio.html', result)

def news_shinsegae(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('신세계'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('신세계'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'shinsegae.html', result)

def news_shinhan(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('신한지주'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('신한지주'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'shinhan.html', result)

def news_amoreg(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('아모레G'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('아모레G'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'amoreg.html', result)

def news_ncsoft(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('엔씨소프트'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('엔씨소프트'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'ncsoft.html', result)

def news_ottugi(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('오뚜기'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('오뚜기'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'ottugi.html', result)

def news_emart(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('이마트'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('이마트'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'emart.html', result)

def news_kakao(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('카카오'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('카카오'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'kakao.html', result)

def news_hana(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('하나금융지주'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('하나금융지주'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'hana.html', result)

def news_hanguk(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('한국금융지주'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('한국금융지주'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'hanguk.html', result)

def news_hanwha(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('한화솔루션'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('한화솔루션'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'hanwha.html', result)

def news_hyundaebuild(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('현대건설'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('현대건설'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'hyundaebuild.html', result)

def news_hyundae(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('현대차'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('현대차'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'hyundae.html', result)

def news_shillahotel(request):
    result = dict()
    db_news = sqlite3.connect('bigkinds.db')
    db_news.row_factory = sqlite3.Row
    c = db_news.cursor()

    # 입력된 기업
    stockname = request.GET.get('stockname')
    result['stockname'] = stockname

    # 기업을 다룬 뉴스기사들
    #c.execute("select title, press, category, date, text from {}_news".format(stockname))
    c.execute("select title, press, category, date, text from {}_news".format('호텔신라'))
    data = c.fetchall()
    result['erows'] = data

    # 뉴스기사 개수
    #c.execute("select count(*) from {}_news".format(stockname))
    c.execute("select count(*) from {}_news".format('호텔신라'))
    cnt_curs = c.fetchone()
    total_cnt =  int(cnt_curs[0])
    result['total_cnt'] = total_cnt

    return render(request, 'shillahotel.html', result)



