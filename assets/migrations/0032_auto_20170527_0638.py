# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-27 06:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0031_auto_20170527_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 27, 6, 38, 48, 993607, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='check',
            name='signature',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='assets.AssetSignature'),
        ),
    ]