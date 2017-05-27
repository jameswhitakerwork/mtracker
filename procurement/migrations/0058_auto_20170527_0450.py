# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-27 04:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0057_auto_20170514_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsignaturemodel',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 27, 4, 50, 33, 535994, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='pr_date_prepared',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 5, 27, 4, 50, 33, 537140, tzinfo=utc), null=True),
        ),
    ]