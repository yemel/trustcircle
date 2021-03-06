# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-10-27 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0011_auto_20181027_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='digest_html',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='digest_text',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='request_html',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='request_text',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
    ]
