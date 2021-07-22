from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'fname', 'lname', 'email', 'subject', 'message')
    list_display_links = ('id', 'lname')
    list_filter = ('id', 'fname', 'email')
    list_per_page = 25

admin.site.register(Contact, NewsAdmin)