# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('second_name', models.CharField(max_length=30, verbose_name='Отчество', blank=True)),
                ('birthday', models.DateField(verbose_name='День рождения')),
                ('residence', models.CharField(max_length=50, verbose_name='Адрес проживания')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='EMail', blank=True)),
                ('photo', models.ImageField(upload_to='', verbose_name='Фотография')),
                ('passport', models.ImageField(upload_to='', verbose_name='Паспорт')),
                ('deposit', models.DecimalField(default=0, verbose_name='Депозит', max_digits=10, decimal_places=2)),
                ('comment', models.TextField(max_length=500, verbose_name='Дополнительный комментарий', blank=True)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='FixedProperty',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('location', models.CharField(unique=True, max_length=50, verbose_name='Местоположение')),
                ('cost', models.DecimalField(default=0, verbose_name='Стоимость', max_digits=10, decimal_places=2)),
                ('owner', models.ForeignKey(to='flatlease.Client')),
            ],
            options={
                'verbose_name': 'Недвижимость',
            },
        ),
    ]
