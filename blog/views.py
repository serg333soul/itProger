from django.shortcuts import render
from .models import News
from django.views.generic import ListView, DetailView

def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Главная страница блога'
    }
    return render(request, 'blog/home.html', data)

class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница блога'
        return ctx

class NewsDetailView(DetailView):
    model = News
    #template_name = 'blog/news_detail.html' вызивается по умолчанию

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Страничка про нас'})
