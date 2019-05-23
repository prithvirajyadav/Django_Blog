# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-13 11:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180713_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 13, 11, 7, 16, 251000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 13, 11, 7, 16, 250000, tzinfo=utc)),
        ),
    ]
