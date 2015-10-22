# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0003_auto_20151011_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('count', models.DecimalField(default=0, verbose_name='Платежа', decimal_places=2, max_digits=10)),
                ('pay_type', models.CharField(default='cash', choices=[('cash', 'Наличные'), ('transfer', 'Перевод'), ('card', 'Банковская карта')], verbose_name='Тип платежа', max_length=20)),
                ('pay_date', models.DateTimeField(verbose_name='Дата платежа')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(upload_to=('client_media/%s_%s', (models.CharField(verbose_name='Фамилия', max_length=30), '<built-in function id>')), verbose_name='Паспорт', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(upload_to=('client_media/%s_%s', (models.CharField(verbose_name='Фамилия', max_length=30), '<built-in function id>')), verbose_name='Фотография', blank=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='owner',
            field=models.ForeignKey(to='flatlease.Client'),
        ),
    ]
