from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    return HttpResponse('<h2>Страница с контактами</h2>')
