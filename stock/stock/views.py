from django.shortcuts import render, redirect



def index(request):
    return render(request, 'index.html')
def main(request):
    return render(request, 'main.html')
def getdata(request):
    return render(request, 'getdata.html')
def team(request):
    return render(request, 'team.html')
# def inner(request):
#     return render(request, 'inner-page.html')