# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 22:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='first_team',
        ),
        migrations.RemoveField(
            model_name='team',
            name='cap',
        ),
        migrations.DeleteModel(
            name='Match',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]