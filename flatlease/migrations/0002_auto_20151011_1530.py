# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fixedproperty',
            options={'verbose_name': 'Недвижимость', 'verbose_name_plural': 'Недвижимость'},
        ),
        migrations.AddField(
            model_name='client',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Время добавления', default=datetime.datetime(2015, 10, 11, 8, 30, 50, 585275, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(verbose_name='Паспорт', upload_to='client_passport'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(verbose_name='Фотография', upload_to='client_photo'),
        ),
    ]
