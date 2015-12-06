# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('car_leasing', '0002_auto_20151206_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='man_date',
            field=models.DateField(verbose_name='Дата выпуска', default=datetime.datetime(2015, 12, 6, 13, 3, 44, 868232, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='model',
            name='year',
            field=models.DateField(verbose_name='Год выпуска', default=datetime.datetime(2015, 12, 6, 13, 3, 44, 867633, tzinfo=utc)),
        ),
    ]
