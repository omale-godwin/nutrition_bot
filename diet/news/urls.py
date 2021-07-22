
from django.urls import path
from . import views
urlpatterns = [
    path('news', views.news, name='news'),
    path('newsdetail', views.newsdetail, name='newsdetail'),
   
   
]
