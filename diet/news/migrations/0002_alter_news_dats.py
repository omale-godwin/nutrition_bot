# Generated by Django 3.2.5 on 2021-07-21 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='dats',
            field=models.DateField(verbose_name=datetime.datetime(2021, 7, 21, 19, 39, 38, 218480)),
        ),
    ]