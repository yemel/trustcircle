# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-09-11 19:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='circle',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 9, 11, 19, 4, 3, 950066, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membership',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 9, 11, 19, 4, 9, 717615, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
