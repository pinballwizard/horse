# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):


    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('second_name', models.CharField(blank=True, max_length=30, verbose_name='Отчество')),
                ('birthday', models.DateField(verbose_name='День рождения')),
                ('residence', models.CharField(max_length=50, verbose_name='Адрес проживания')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='EMail')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фотография')),
                ('passport', models.ImageField(upload_to='', verbose_name='Паспорт')),
                ('deposit', models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Депозит')),
                ('comment', models.TextField(blank=True, max_length=500, verbose_name='Дополнительный комментарий')),
            ],
            options={
                'verbose_name_plural': 'Клиенты',
                'verbose_name': 'Клиент',
            },
        ),
        migrations.CreateModel(
            name='FixedProperty',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('location', models.CharField(unique=True, max_length=50, verbose_name='Местоположение')),
                ('cost', models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Стоимость')),
                ('owner', models.ForeignKey(to='flatlease.Client')),
            ],
            options={
                'verbose_name': 'Недвижимость',
            },
        ),
        migrations.AlterModelOptions(
            name='fixedproperty',
            options={'verbose_name_plural': 'Недвижимость', 'verbose_name': 'Недвижимость'},
        ),
        migrations.AddField(
            model_name='client',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 11, 8, 30, 50, 585275, tzinfo=utc), auto_now_add=True, verbose_name='Время добавления'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(upload_to='client_passport', verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(upload_to='client_photo', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(blank=True, upload_to='client_passport', verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to='client_photo', verbose_name='Фотография'),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('count', models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Платежа')),
                ('pay_type', models.CharField(default='cash', choices=[('cash', 'Наличные'), ('transfer', 'Перевод'), ('card', 'Банковская карта')], max_length=20, verbose_name='Тип платежа')),
                ('pay_date', models.DateTimeField(verbose_name='Дата платежа')),
            ],
            options={
                'verbose_name_plural': 'Платежи',
                'verbose_name': 'Платеж',
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Фотография'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='owner',
            field=models.ForeignKey(to='flatlease.Client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='count',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Платеж'),
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='pay_date',
            new_name='pub_date',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата платежа'),
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='pay_type',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(default='cash', choices=[('cash', 'Наличные'), ('transfer', 'Перевод'), ('card', 'Банковская карта'), ('inside', 'Внутренний перевод')], max_length=20, verbose_name='Тип платежа'),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Фотография'),
        ),
        migrations.RemoveField(
            model_name='client',
            name='deposit',
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='fixedproperty',
            name='owner',
            field=models.ForeignKey(to='flatlease.Client', verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='client',
            name='monthly_payment',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, editable=False, verbose_name='Ежемесячный платеж'),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Фотография'),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('type', models.CharField(default='application', choices=[('application', 'Заявление'), ('form', 'Анкета'), ('contract', 'Договор')], max_length=20, verbose_name='Тип')),
                ('document', models.FileField(upload_to=models.ForeignKey(to='flatlease.Client', verbose_name='Клиент'), verbose_name='Документ')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
            ],
            options={
                'verbose_name_plural': 'Документы',
                'verbose_name': 'Документ',
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Фотография'),
        ),
        migrations.AddField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(to='flatlease.Client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to=('client_media/%s_%s', (models.CharField(max_length=30, verbose_name='Фамилия'), '<built-in function id>')), verbose_name='Фотография'),
        ),
    ]
