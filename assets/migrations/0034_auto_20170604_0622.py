# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-04 06:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0033_auto_20170604_0600'),
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
            field=models.DateField(default=datetime.datetime(2017, 6, 4, 6, 22, 35, 651170, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='check',
            name='signature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.AssetSignature'),
        ),
    ]