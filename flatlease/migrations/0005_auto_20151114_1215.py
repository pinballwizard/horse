# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import flatlease.models


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0004_auto_20151114_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(upload_to=flatlease.models.photo_file_path, verbose_name='Фотография', blank=True),
        ),
        migrations.AlterField(
            model_name='passport',
            name='image',
            field=models.ImageField(upload_to=flatlease.models.content_file_path, verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='number',
            field=models.IntegerField(verbose_name='Серия и Номер'),
        ),
    ]
