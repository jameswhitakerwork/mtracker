# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-04 07:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0065_auto_20170604_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsignaturemodel',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 6, 4, 7, 52, 36, 428191, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='pr_date_prepared',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 6, 4, 7, 52, 36, 429152, tzinfo=utc), null=True),
        ),
    ]
