# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0002_auto_20151108_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('number', models.IntegerField(verbose_name='Серия')),
                ('data', models.DateField(verbose_name='Дата выдачи')),
                ('whom', models.TextField(verbose_name='Кем выдан', max_length=100)),
                ('image', models.ImageField(upload_to='<built-in function id>', blank=True, verbose_name='Паспорт')),
            ],
            options={
                'verbose_name_plural': 'Паспортов',
                'verbose_name': 'Паспорт',
            },
        ),
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('pub_date', models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=30)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('second_name', models.CharField(blank=True, verbose_name='Отчество', max_length=30)),
                ('birthday', models.DateField(blank=True, verbose_name='День рождения')),
                ('phone', models.CharField(verbose_name='Телефон', max_length=12)),
                ('residence', models.CharField(verbose_name='Адрес проживания', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Родственники',
                'verbose_name': 'Родственник',
            },
        ),
        migrations.CreateModel(
            name='Spouse',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('pub_date', models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=30)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('second_name', models.CharField(blank=True, verbose_name='Отчество', max_length=30)),
                ('birthday', models.DateField(blank=True, verbose_name='День рождения')),
                ('phone', models.CharField(verbose_name='Телефон', max_length=12)),
                ('residence', models.CharField(verbose_name='Адрес проживания', max_length=100)),
                ('workplace', models.CharField(blank=True, verbose_name='Место работы', max_length=50)),
                ('work_position', models.CharField(blank=True, verbose_name='Должность', max_length=50)),
                ('salary', models.DecimalField(max_digits=10, verbose_name='Заработная плата', decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Родственники',
                'verbose_name': 'Родственник',
            },
        ),
        migrations.RemoveField(
            model_name='client',
            name='passport',
        ),
        migrations.AddField(
            model_name='client',
            name='birthplace',
            field=models.CharField(default='krasnodar', verbose_name='Место рождения', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='health',
            field=models.CharField(blank=True, verbose_name='Состояние здоровья', max_length=20),
        ),
        migrations.AddField(
            model_name='client',
            name='profit',
            field=models.DecimalField(default=10, max_digits=10, blank=True, verbose_name='Дополнительный доход', decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='registration',
            field=models.CharField(default='krasnodar', verbose_name='Регистрация по месту жительства', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='salary',
            field=models.DecimalField(default=10, max_digits=10, verbose_name='Заработная плата', decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='work_position',
            field=models.CharField(blank=True, verbose_name='Должность', max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='workplace',
            field=models.CharField(blank=True, verbose_name='Место работы', max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(blank=True, verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(verbose_name='Телефон', max_length=12),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(upload_to='<built-in function id>', blank=True, verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='client',
            name='residence',
            field=models.CharField(verbose_name='Адрес проживания', max_length=100),
        ),
        migrations.AddField(
            model_name='spouse',
            name='owner',
            field=models.OneToOneField(to='flatlease.Client', verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='relative',
            name='owner',
            field=models.ForeignKey(to='flatlease.Client', verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='passport',
            name='owner',
            field=models.OneToOneField(to='flatlease.Client', verbose_name='Клиент'),
        ),
    ]
