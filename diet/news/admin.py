from django.contrib import admin
from .models import News
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photos', 'desc', 'dats')
    list_display_links = ('id', 'title')
    list_filter = ('id', 'title')
    list_per_page = 25

admin.site.register(News, NewsAdmin)