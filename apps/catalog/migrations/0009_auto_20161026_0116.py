# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-25 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20161026_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='广告描述'),
        ),
    ]
