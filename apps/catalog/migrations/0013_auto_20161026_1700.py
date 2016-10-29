# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-26 09:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_ads_callback_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='ads',
            name='callback_url',
            field=models.URLField(blank=True, default=datetime.datetime(2016, 10, 26, 9, 0, 40, 759811, tzinfo=utc), verbose_name='回调url'),
            preserve_default=False,
        ),
    ]
