# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_pictures_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]