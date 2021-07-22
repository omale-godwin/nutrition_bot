from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import News
# Create your views here.
def news(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'news/news.html', context)

def newsdetail(request, new_id):
    
    return render(request, 'news/newsdetail.html')