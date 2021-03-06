# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-06 04:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hr', '0010_auto_20170504_0230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateField()),
                ('reportee', models.EmailField(max_length=254)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Program')),
            ],
        ),
    ]
