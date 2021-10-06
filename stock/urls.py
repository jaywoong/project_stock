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

    path('news', views.news),
    path('news_amore', views.news_amore),
    path('news_hanmi', views.news_hanmi),
    path('news_hmm', views.news_hmm),
    path('news_lg', views.news_lg),
    path('news_nh', views.news_nh),
    path('news_orion', views.news_orion),
    # path('inner-page.html', views.inner, name='inner'),


]
