# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-04 07:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0036_auto_20170604_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 6, 4, 7, 44, 16, 141812, tzinfo=utc)),
        ),
    ]