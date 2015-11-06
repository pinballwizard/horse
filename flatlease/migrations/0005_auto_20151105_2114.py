# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0004_auto_20151021_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('type', models.CharField(verbose_name='Тип', default='application', choices=[('application', 'Заявление'), ('form', 'Анкета'), ('contract', 'Договор')], max_length=20)),
                ('name', models.CharField(verbose_name='Имя', max_length=20)),
                ('pub_date', models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(verbose_name='Паспорт', blank=True, upload_to=('client_media/%s_%s', (models.CharField(verbose_name='Фамилия', max_length=30), '<built-in function id>'))),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(verbose_name='Фотография', blank=True, upload_to=('client_media/%s_%s', (models.CharField(verbose_name='Фамилия', max_length=30), '<built-in function id>'))),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='count',
            field=models.DecimalField(decimal_places=2, verbose_name='Платеж', default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='pay_date',
            field=models.DateTimeField(verbose_name='Дата платежа', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='pay_type',
            field=models.CharField(verbose_name='Тип платежа', default='cash', choices=[('cash', 'Наличные'), ('transfer', 'Перевод'), ('card', 'Банковская карта'), ('inside', 'Внутренний перевод')], max_length=20),
        ),
        migrations.AddField(
            model_name='documents',
            name='owner',
            field=models.ForeignKey(to='flatlease.Client'),
        ),
    ]
