from django.shortcuts import render, redirect




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

def newsdata(request):
    category = request.GET['category'];
    date = request.GET['date'];
    press = request.GET['press'];
    text = request.GET['text'];
    title = request.GET['title'];
    return render(request, 'news.html');
