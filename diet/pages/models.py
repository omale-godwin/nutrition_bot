from django.core.checks import messages
from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.fname

