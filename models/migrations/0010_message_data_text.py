# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-10-17 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0009_auto_20181016_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='data_text',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
    ]
