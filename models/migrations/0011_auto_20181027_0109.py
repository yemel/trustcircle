# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-10-27 01:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0010_message_data_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='diggest_date',
            new_name='digest_date',
        ),
    ]
