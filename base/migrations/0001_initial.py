# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import base.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('pub_date', models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=30)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('second_name', models.CharField(verbose_name='Отчество', blank=True, max_length=30)),
                ('birthday', models.DateField(verbose_name='День рождения')),
                ('phone', models.CharField(verbose_name='Телефон', blank=True, max_length=12)),
                ('residence', models.CharField(verbose_name='Адрес проживания', blank=True, max_length=100)),
                ('email', models.EmailField(verbose_name='EMail', blank=True, max_length=254)),
                ('health', models.CharField(verbose_name='Состояние здоровья', max_length=50, default='Здоров', choices=[('Здоров', 'Здоров'), ('Серьезные проблемы со здоровьем', 'Серьезные проблемы со здоровьем'), ('На учете в наркодиспансере', 'На учете в наркодиспансере'), ('На учете в психдиспансере', 'На учете в психдиспансере')])),
                ('workplace', models.CharField(verbose_name='Место работы', blank=True, max_length=50)),
                ('work_position', models.CharField(verbose_name='Должность', blank=True, max_length=50)),
                ('salary', models.DecimalField(verbose_name='Заработная плата', decimal_places=2, default=0, max_digits=10)),
                ('profit', models.DecimalField(verbose_name='Дополнительный доход', decimal_places=2, default=0, max_digits=10)),
                ('photo', models.ImageField(verbose_name='Фотография', upload_to=base.models.photo_file_path, default='/static/flatlease/images/userPlaceholder.png')),
                ('monthly_payment', models.DecimalField(verbose_name='Ежемесячный платеж', decimal_places=2, default=0, max_digits=10)),
                ('comment', models.TextField(verbose_name='Дополнительный комментарий', blank=True, max_length=500)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type', models.CharField(verbose_name='Тип', max_length=20, default='Заявление', choices=[('Заявление', 'Заявление'), ('Анкета', 'Анкета'), ('Договор', 'Договор')])),
                ('document', models.FileField(verbose_name='Документ', upload_to=base.models.content_file_path)),
                ('pub_date', models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('pub_date', models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=30)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('second_name', models.CharField(verbose_name='Отчество', blank=True, max_length=30)),
                ('birthday', models.DateField(verbose_name='День рождения')),
                ('phone', models.CharField(verbose_name='Телефон', blank=True, max_length=12)),
                ('residence', models.CharField(verbose_name='Адрес проживания', blank=True, max_length=100)),
                ('relation', models.CharField(verbose_name='Родство', max_length=10, default='Отец', choices=[('Отец', 'Отец'), ('Мать', 'Мать'), ('Ребенок', 'Ребенок')])),
            ],
            options={
                'verbose_name': 'Родственник',
                'verbose_name_plural': 'Родственники',
            },
        ),
        migrations.CreateModel(
            name='Spouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('pub_date', models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=30)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('second_name', models.CharField(verbose_name='Отчество', blank=True, max_length=30)),
                ('birthday', models.DateField(verbose_name='День рождения')),
                ('phone', models.CharField(verbose_name='Телефон', blank=True, max_length=12)),
                ('residence', models.CharField(verbose_name='Адрес проживания', blank=True, max_length=100)),
                ('workplace', models.CharField(verbose_name='Место работы', blank=True, max_length=50)),
                ('work_position', models.CharField(verbose_name='Должность', blank=True, max_length=50)),
                ('salary', models.DecimalField(verbose_name='Заработная плата', decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Супруг(а)',
                'verbose_name_plural': 'Супруги',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('count', models.DecimalField(verbose_name='Платеж', decimal_places=2, default=0, max_digits=10)),
                ('type', models.CharField(verbose_name='Тип платежа', max_length=20, default='Наличные', choices=[('Наличные', 'Наличные'), ('Безналичный', 'Безналичный'), ('Внутренний', 'Внутренний перевод')])),
                ('pub_date', models.DateTimeField(verbose_name='Дата платежа', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('owner', models.OneToOneField(serialize=False, verbose_name='Клиент', primary_key=True, to='base.Client')),
                ('number', models.CharField(verbose_name='Серия и Номер', max_length=10)),
                ('date', models.DateField(verbose_name='Дата выдачи')),
                ('whom', models.TextField(verbose_name='Кем выдан', max_length=100)),
                ('image', models.ImageField(verbose_name='Паспорт', upload_to=base.models.content_file_path)),
                ('birthplace', models.CharField(verbose_name='Место рождения', max_length=100)),
                ('registration', models.CharField(verbose_name='Регистрация по месту жительства', max_length=100)),
            ],
            options={
                'verbose_name': 'Паспорт',
                'verbose_name_plural': 'Паспорта',
            },
        ),
        migrations.AddField(
            model_name='transaction',
            name='owner',
            field=models.ForeignKey(verbose_name='Клиент', to='base.Client'),
        ),
        migrations.AddField(
            model_name='spouse',
            name='owner',
            field=models.OneToOneField(to='base.Client', verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='relative',
            name='owner',
            field=models.ForeignKey(verbose_name='Клиент', to='base.Client'),
        ),
        migrations.AddField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(verbose_name='Клиент', to='base.Client'),
        ),
        migrations.AddField(
            model_name='client',
            name='manager',
            field=models.ForeignKey(verbose_name='Менеджер', to=settings.AUTH_USER_MODEL),
        ),
    ]
