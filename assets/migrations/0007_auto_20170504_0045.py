# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 00:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_auto_20170503_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 4, 0, 45, 21, 442811, tzinfo=utc)),
        ),
    ]