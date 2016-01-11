# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_leasing', '0006_auto_20151212_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='cost',
            field=models.DecimalField(default=0, verbose_name='Стоимость', decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='car',
            name='number',
            field=models.CharField(blank=True, verbose_name='Гос. Номер', max_length=6),
        ),
        migrations.AddField(
            model_name='car',
            name='payed',
            field=models.DecimalField(default=0, verbose_name='Уплачено', decimal_places=2, max_digits=10),
        ),
        migrations.AddField(
            model_name='car',
            name='region',
            field=models.CharField(blank=True, default=23, verbose_name='Регион', max_length=2),
        ),
    ]
