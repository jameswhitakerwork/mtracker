# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-14 12:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0027_auto_20170507_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('desposed', 'desposed'), ('lost_missing_stolen', 'lost, missing or stolen')], default='active', max_length=32),
        ),
        migrations.AlterField(
            model_name='check',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 14, 12, 20, 45, 326034, tzinfo=utc)),
        ),
    ]
