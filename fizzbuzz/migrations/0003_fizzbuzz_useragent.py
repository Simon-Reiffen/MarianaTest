# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-29 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fizzbuzz', '0002_auto_20151129_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='fizzbuzz',
            name='useragent',
            field=models.TextField(default=' '),
        ),
    ]
