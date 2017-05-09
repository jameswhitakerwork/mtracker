# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 11:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0053_auto_20170506_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsignaturemodel',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 7, 11, 47, 42, 394778, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='pr_date_prepared',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 7, 11, 47, 42, 395782, tzinfo=utc), null=True),
        ),
    ]
