# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_auto_20161110_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.SlugField(unique=True),
        ),
    ]
