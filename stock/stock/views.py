from django.shortcuts import render, redirect



def index(request):
    return render(request, 'index.html')
def main(request):
    return render(request, 'main.html')
# def inner(request):
#     return render(request, 'inner-page.html')