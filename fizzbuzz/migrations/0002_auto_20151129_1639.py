# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-29 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fizzbuzz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fizzbuzz',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]