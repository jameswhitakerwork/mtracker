# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-27 05:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0030_auto_20170527_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 27, 5, 46, 55, 999136, tzinfo=utc)),
        ),
    ]
