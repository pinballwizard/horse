# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('car_leasing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Производитель', 'verbose_name_plural': 'Производители'},
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterModelOptions(
            name='model',
            options={'verbose_name': 'Модель', 'verbose_name_plural': 'Модели'},
        ),
        migrations.AddField(
            model_name='model',
            name='year',
            field=models.DateField(verbose_name='Год выпуска', default=datetime.date(2015, 12, 6)),
        ),
        migrations.AlterField(
            model_name='car',
            name='man_date',
            field=models.DateField(verbose_name='Дата выпуска', default=datetime.date(2015, 12, 6)),
        ),
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(verbose_name='Пробег', default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(verbose_name='Клиент', to='base.Client'),
        ),
    ]
