# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_leasing', '0005_auto_20151210_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car_leasing.Model', verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='model',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car_leasing.Brand', verbose_name='Производитель'),
        ),
    ]
