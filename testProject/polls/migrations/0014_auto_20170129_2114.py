# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_books_date_of_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]
