# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0005_auto_20151206_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixedproperty',
            name='build_year',
            field=models.DateField(verbose_name='Дата постройки', default=datetime.datetime(2015, 12, 6, 13, 3, 44, 865384, tzinfo=utc)),
        ),
    ]
