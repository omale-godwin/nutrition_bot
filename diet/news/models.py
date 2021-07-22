from django.db import models
from datetime import datetime
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=200)
    photos= models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    dats = models.DateField(datetime.now())
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.title