# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-06 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0010_auto_20170504_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='desc',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]