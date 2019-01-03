from django.shortcuts import render

from django.http import HttpResponse

news = [
    {
    'title': 'Наша первая запись',
    'text': 'Текст до первой записи',
    'date': '03.01.18',
    'avtor': 'Георгий'
    },
    {
    'title': 'Наша вторая запись',
    'text': 'Текст для второй записи',
    'date': '03.01.18',
    'avtor': 'Джон'
    }

]

def home(request):
    date = {
        'news': news,
        'title': 'Главная страница блога'
    }
    return render(request, 'blog/home.html')

def contact(request):
    return render(request, 'blog/contact.html')
