# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-24 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beltexam', '0003_auto_20181024_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='categories',
            field=models.CharField(max_length=255),
        ),
    ]
