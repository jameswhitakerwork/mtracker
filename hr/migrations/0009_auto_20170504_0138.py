# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 01:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0008_auto_20170504_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.Program'),
        ),
    ]
