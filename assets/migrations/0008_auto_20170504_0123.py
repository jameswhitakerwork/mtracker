# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 01:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_auto_20170504_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 4, 1, 23, 18, 371238, tzinfo=utc)),
        ),
    ]
