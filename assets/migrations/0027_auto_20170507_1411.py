# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 14:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0026_auto_20170507_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 7, 14, 11, 12, 859950, tzinfo=utc)),
        ),
    ]
