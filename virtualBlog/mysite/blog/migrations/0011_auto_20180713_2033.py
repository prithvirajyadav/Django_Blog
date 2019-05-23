# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-13 15:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180713_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 13, 15, 3, 24, 507000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 13, 15, 3, 24, 506000, tzinfo=utc)),
        ),
    ]
