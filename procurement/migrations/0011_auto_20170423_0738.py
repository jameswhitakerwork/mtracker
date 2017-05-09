# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 07:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0010_auto_20170423_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaserequest',
            name='pr_no',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='pr_date_prepared',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 4, 23, 7, 38, 32, 98529, tzinfo=utc), null=True),
        ),
    ]
