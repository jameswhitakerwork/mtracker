# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-04 06:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0062_auto_20170604_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsignaturemodel',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 6, 4, 6, 50, 26, 863383, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='pr_date_prepared',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 6, 4, 6, 50, 26, 864360, tzinfo=utc), null=True),
        ),
    ]
