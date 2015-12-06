# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('car_leasing', '0002_auto_20151206_1930'),
        ('flatlease', '0004_auto_20151206_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='document',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='passport',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='relative',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='spouse',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='owner',
        ),
        migrations.AddField(
            model_name='fixedproperty',
            name='build_year',
            field=models.DateField(verbose_name='Дата постройки', default=datetime.date(2015, 12, 6)),
        ),
        migrations.AddField(
            model_name='fixedproperty',
            name='number',
            field=models.CharField(verbose_name='Кадастровый номер', blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='fixedproperty',
            name='owner',
            field=models.ForeignKey(verbose_name='Клиент', to='base.Client'),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Passport',
        ),
        migrations.DeleteModel(
            name='Relative',
        ),
        migrations.DeleteModel(
            name='Spouse',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
