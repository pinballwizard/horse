# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import flatlease.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('pub_date', models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=30)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('second_name', models.CharField(blank=True, verbose_name='Отчество', max_length=30)),
                ('birthday', models.DateField(blank=True, verbose_name='День рождения')),
                ('phone', models.CharField(blank=True, verbose_name='Телефон', max_length=12)),
                ('residence', models.CharField(blank=True, verbose_name='Адрес проживания', max_length=100)),
                ('email', models.EmailField(blank=True, verbose_name='EMail', max_length=254)),
                ('health', models.CharField(verbose_name='Состояние здоровья', choices=[('healthy', 'Здоров'), ('sick', 'Болен'), ('addict', 'Наркодиспансер'), ('psycho', 'Психодиспансер')], default='healthy', max_length=20)),
                ('workplace', models.CharField(blank=True, verbose_name='Место работы', max_length=50)),
                ('work_position', models.CharField(blank=True, verbose_name='Должность', max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, verbose_name='Заработная плата', max_digits=10, default=0)),
                ('profit', models.DecimalField(decimal_places=2, verbose_name='Дополнительный доход', max_digits=10, default=0)),
                ('photo', models.ImageField(blank=True, verbose_name='Фотография', upload_to=flatlease.models.photo_file_path)),
                ('monthly_payment', models.DecimalField(decimal_places=2, verbose_name='Ежемесячный платеж', max_digits=10, default=0)),
                ('comment', models.TextField(blank=True, verbose_name='Дополнительный комментарий', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Клиенты',
                'verbose_name': 'Клиент',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type', models.CharField(verbose_name='Тип', choices=[('application', 'Заявление'), ('form', 'Анкета'), ('contract', 'Договор')], default='application', max_length=20)),
                ('document', models.FileField(verbose_name='Документ', upload_to=flatlease.models.content_file_path)),
                ('pub_date', models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Документы',
                'verbose_name': 'Документ',
            },
        ),
        migrations.CreateModel(
            name='FixedProperty',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('location', models.CharField(unique=True, verbose_name='Местоположение', max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, verbose_name='Стоимость', max_digits=10, default=0)),
            ],
            options={
                'verbose_name_plural': 'Недвижимость',
                'verbose_name': 'Недвижимость',
            },
        ),
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('pub_date', models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=30)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('second_name', models.CharField(blank=True, verbose_name='Отчество', max_length=30)),
                ('birthday', models.DateField(blank=True, verbose_name='День рождения')),
                ('phone', models.CharField(blank=True, verbose_name='Телефон', max_length=12)),
                ('residence', models.CharField(blank=True, verbose_name='Адрес проживания', max_length=100)),
                ('relation', models.CharField(verbose_name='Отношение', choices=[('father', 'Отец'), ('mother', 'Мать'), ('child', 'Ребенок')], default='father', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Родственники',
                'verbose_name': 'Родственник',
            },
        ),
        migrations.CreateModel(
            name='Spouse',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('pub_date', models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=30)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('second_name', models.CharField(blank=True, verbose_name='Отчество', max_length=30)),
                ('birthday', models.DateField(blank=True, verbose_name='День рождения')),
                ('phone', models.CharField(blank=True, verbose_name='Телефон', max_length=12)),
                ('residence', models.CharField(blank=True, verbose_name='Адрес проживания', max_length=100)),
                ('workplace', models.CharField(blank=True, verbose_name='Место работы', max_length=50)),
                ('work_position', models.CharField(blank=True, verbose_name='Должность', max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, verbose_name='Заработная плата', max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Супруги',
                'verbose_name': 'Супруг(а)',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('count', models.DecimalField(decimal_places=2, verbose_name='Платеж', max_digits=10, default=0)),
                ('type', models.CharField(verbose_name='Тип платежа', choices=[('cash', 'Наличные'), ('transfer', 'Перевод'), ('card', 'Банковская карта'), ('inside', 'Внутренний перевод')], default='cash', max_length=20)),
                ('pub_date', models.DateTimeField(verbose_name='Дата платежа', auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Платежи',
                'verbose_name': 'Платеж',
            },
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('owner', models.OneToOneField(verbose_name='Клиент', to='flatlease.Client', serialize=False, primary_key=True)),
                ('number', models.CharField(verbose_name='Серия и Номер', max_length=10)),
                ('data', models.DateField(verbose_name='Дата выдачи')),
                ('whom', models.TextField(verbose_name='Кем выдан', max_length=100)),
                ('image', models.ImageField(verbose_name='Паспорт', upload_to=flatlease.models.content_file_path)),
                ('birthplace', models.CharField(verbose_name='Место рождения', max_length=100)),
                ('registration', models.CharField(verbose_name='Регистрация по месту жительства', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Паспорта',
                'verbose_name': 'Паспорт',
            },
        ),
        migrations.AddField(
            model_name='transaction',
            name='owner',
            field=models.ForeignKey(verbose_name='Клиент', to='flatlease.Client'),
        ),
        migrations.AddField(
            model_name='spouse',
            name='owner',
            field=models.OneToOneField(verbose_name='Клиент', to='flatlease.Client'),
        ),
        migrations.AddField(
            model_name='relative',
            name='owner',
            field=models.ForeignKey(verbose_name='Клиент', to='flatlease.Client'),
        ),
        migrations.AddField(
            model_name='fixedproperty',
            name='owner',
            field=models.ForeignKey(verbose_name='Клиент', to='flatlease.Client'),
        ),
        migrations.AddField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(verbose_name='Клиент', to='flatlease.Client'),
        ),
        migrations.AddField(
            model_name='client',
            name='manager',
            field=models.ForeignKey(verbose_name='Менеджер', to=settings.AUTH_USER_MODEL),
        ),
    ]
