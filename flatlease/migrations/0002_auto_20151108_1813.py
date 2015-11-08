# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0001_squashed_0006_auto_20151108_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Паспорт', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Фотография', blank=True),
        ),
    ]
