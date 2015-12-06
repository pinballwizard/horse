# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(verbose_name='День рождения', default=datetime.datetime(2015, 12, 6, 13, 3, 44, 858629, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='relative',
            name='birthday',
            field=models.DateField(verbose_name='День рождения', default=datetime.datetime(2015, 12, 6, 13, 3, 44, 858629, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='birthday',
            field=models.DateField(verbose_name='День рождения', default=datetime.datetime(2015, 12, 6, 13, 3, 44, 858629, tzinfo=utc)),
        ),
    ]
