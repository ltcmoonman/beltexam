# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-24 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beltexam', '0007_auto_20181024_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='categories',
            field=models.TextField(max_length=255),
        ),
    ]
