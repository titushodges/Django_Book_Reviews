# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0002_auto_20160901_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
