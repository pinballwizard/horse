# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-10 13:48
from __future__ import unicode_literals

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20151206_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to=base.models.photo_file_path, verbose_name='Фотография'),
        ),
    ]
