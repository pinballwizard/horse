# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0002_auto_20151011_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(upload_to='client_passport', blank=True, verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(upload_to='client_photo', blank=True, verbose_name='Фотография'),
        ),
    ]
