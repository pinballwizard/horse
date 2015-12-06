# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0004_auto_20151206_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Производитель', max_length=50)),
                ('logo', models.ImageField(verbose_name='Лого', blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('color', models.CharField(verbose_name='Цвет', blank=True, max_length=50)),
                ('man_date', models.DateField(verbose_name='Дата выпуска', blank=True)),
                ('mileage', models.IntegerField(verbose_name='Пробег', blank=True)),
                ('photo', models.ImageField(verbose_name='Фотография', blank=True, upload_to='')),
                ('comment', models.TextField(verbose_name='Комментарий', blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Модель', max_length=50)),
                ('brand', models.ForeignKey(verbose_name='Производитель', to='car_leasing.Brand', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(verbose_name='Производитель', to='car_leasing.Model', blank=True),
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(verbose_name='Клиент', to='flatlease.Client'),
        ),
    ]
