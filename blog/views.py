from django.shortcuts import render
from .models import News

news = [
    {
    'title': 'Наша первая запись',
    'text': 'Текст для первой записи',
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
    data = {
        'news': News.objects.all(),
        'title': 'Главная страница блога'
    }
    return render(request, 'blog/home.html', data)

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Страничка про нас'})
