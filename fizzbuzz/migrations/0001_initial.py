# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-29 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fizzbuzz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
