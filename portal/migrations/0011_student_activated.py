# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-16 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_auto_20170715_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='activated',
            field=models.BooleanField(default=False),
        ),
    ]
