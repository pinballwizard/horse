# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0006_auto_20151105_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='document',
            field=models.FileField(upload_to='', verbose_name='Документ', default=datetime.datetime(2015, 11, 5, 14, 30, 11, 811111, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), blank=True, verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), blank=True, verbose_name='Фотография'),
        ),
    ]
