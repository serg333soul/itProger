from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('<h2>Hello world</h2>')

def contact(request):
    return HttpResponse('<h2>Страница с контактами</h2>')
