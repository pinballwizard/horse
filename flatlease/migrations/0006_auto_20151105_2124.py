# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0005_auto_20151105_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(verbose_name='Паспорт', upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(verbose_name='Фотография', upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), blank=True),
        ),
    ]
