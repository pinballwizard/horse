# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_leasing', '0003_auto_20151206_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='man_date',
            field=models.DateField(verbose_name='Дата выпуска'),
        ),
        migrations.AlterField(
            model_name='model',
            name='year',
            field=models.DateField(verbose_name='Год выпуска'),
        ),
    ]
