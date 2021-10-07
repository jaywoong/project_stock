"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from stock import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('main.html', views.main, name='main'),
    path('getdata.html', views.getdata, name='getdata'),
    path('mgetdata.html', views.mgetdata, name='mgetdata'),
    path('team.html', views.team, name='team'),
    path('news.html', views.news, name='news'),
    path('amore.html', views.news_amore, name='amore'),
    path('hanmi.html', views.news_hanmi, name='hanmi'),
    path('hmm.html', views.news_hmm, name='hmm'),
    path('lg.html', views.news_lg, name='lg'),
    path('nh.html', views.news_nh, name='nh'),
    path('orion.html', views.news_orion, name='orion'),
    path('portpolio.html', views.portpolio, name='portpolio'),
    path('amoreg.html', views.news_amoreg, name='amoreg'),
    path('celltrion.html', views.news_celltrion, name='celltrion'),
    path('cj.html', views.news_cj, name='cj'),
    path('CJENM.html', views.news_CJENM, name='CJENM'),
    path('daehan.html', views.news_daehan, name='daehan'),
    path('emart.html', views.news_emart, name='emart'),
    path('goryeo.html', views.news_goryeo, name='goryeo'),
    path('gs.html', views.news_gs, name='gs'),
    path('hana.html', views.news_hana, name='hana'),
    path('hanguk.html', views.news_hanguk, name='hanguk'),
    path('hanwha.html', views.news_hanwha, name='hanwha'),
    path('hyundae.html', views.news_hyundae, name='hyundae'),
    path('hyundaebuild.html', views.news_hyundaebuild, name='hyundaebuild'),
    path('kakao.html', views.news_kakao, name='kakao'),
    path('kangwon.html', views.news_kangwon, name='kangwon'),
    path('kb.html', views.news_kb, name='kb'),
    path('kia.html', views.news_kia, name='kia'),
    path('kt.html', views.news_kt, name='kt'),
    path('lg2.html', views.news_lg2, name='lg2'),
    path('lg3.html', views.news_lg3, name='lg3'),
    path('lg4.html', views.news_lg4, name='lg4'),
    path('lotte.html', views.news_lotte, name='lotte'),
    path('ls.html', views.news_ls, name='ls'),
    path('mirae.html', views.news_mirae, name='mirae'),
    path('naver.html', views.news_naver, name='naver'),
    path('ncsoft.html', views.news_ncsoft, name='ncsoft'),
    path('netmarble.html', views.news_netmarble, name='netmarble'),
    path('ottugi.html', views.news_ottugi, name='ottugi'),
    path('posco.html', views.news_posco, name='posco'),
    path('samsung.html', views.news_samsung, name='samsung'),
    path('samsungbio.html', views.news_samsungbio, name='samsungbio'),
    path('samsungelectronic.html', views.news_samsungelectronic, name='samsungelectronic'),
    path('samsungengine.html', views.news_samsungengine, name='samsungengine'),
    path('samsungfire.html', views.news_samsungfire, name='samsungfire'),
    path('samsunglife.html', views.news_samsunglife, name='samsunglife'),
    path('samsungsds.html', views.news_samsungsds, name='samsungsds'),
    path('shillahotel.html', views.news_shillahotel, name='shillahotel'),
    path('shinhan.html', views.news_shinhan, name='shinhan'),
    path('shinsegae.html', views.news_shinsegae, name='shinsegae'),
    path('sk.html', views.news_sk, name='sk'),
    path('skh.html', views.news_skh, name='skh'),
    path('skt.html', views.news_skt, name='skt'),
    path('soil.html', views.news_soil, name='soil'),
    path('studio.html', views.news_studio, name='studio'),




    path('news', views.news),
    path('news_amore', views.news_amore),
    path('news_hanmi', views.news_hanmi),
    path('news_hmm', views.news_hmm),
    path('news_lg', views.news_lg),
    path('news_nh', views.news_nh),
    path('news_orion', views.news_orion),
    path('news_amoreg', views.news_amoreg),
    path('news_celltrion', views.news_celltrion),
    path('news_cj', views.news_cj),
    path('news_CJENM', views.news_CJENM),
    path('news_daehan', views.news_daehan),
    path('news_emart', views.news_emart),
    path('news_goryeo', views.news_goryeo),
    path('news_gs', views.news_gs),
    path('news_hana', views.news_hana),
    path('news_hanguk', views.news_hanguk),
    path('news_hanwha', views.news_hanwha),
    path('news_hyundae', views.news_hyundae),
    path('news_hyundaebuild', views.news_hyundaebuild),
    path('news_kakao', views.news_kakao),
    path('news_kangwon', views.news_kangwon),
    path('news_kb', views.news_kb),
    path('news_kia', views.news_kia),
    path('news_kt', views.news_kt),
    path('news_lg2', views.news_lg2),
    path('news_lg3', views.news_lg3),
    path('news_lg4', views.news_lg4),
    path('news_lotte', views.news_lotte),
    path('news_ls', views.news_ls),
    path('news_mirae', views.news_mirae),
    path('news_naver', views.news_naver),
    path('news_ncsoft', views.news_ncsoft),
    path('news_netmarble', views.news_netmarble),
    path('news_ottugi', views.news_ottugi),
    path('news_posco', views.news_posco),
    path('news_samsung', views.news_samsung),
    path('news_samsungbio', views.news_samsungbio),
    path('news_samsungelectronic', views.news_samsungelectronic),
    path('news_samsungengine', views.news_samsungengine),
    path('news_samsunglife', views.news_samsunglife),
    path('news_samsungfire', views.news_samsungfire),
    path('news_samsungsds', views.news_samsungsds),
    path('news_shillahotel', views.news_shillahotel),
    path('news_shinhan', views.news_shinhan),
    path('news_shinsegae', views.news_shinsegae),
    path('news_sk', views.news_sk),
    path('news_skh', views.news_skh),
    path('news_skt', views.news_skt),
    path('news_soil', views.news_soil),
    path('news_studio', views.news_studio),


]
