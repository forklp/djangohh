# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-01-27 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-pub_time',),
            },
        ),
    ]
