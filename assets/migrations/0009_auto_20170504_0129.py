# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 01:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_auto_20170504_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 4, 1, 29, 28, 892352, tzinfo=utc)),
        ),
    ]
