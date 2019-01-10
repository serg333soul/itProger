from django.urls import path
from . import views
urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='blog-home'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('about/', views.contact, name='blog-contacts'),
]
