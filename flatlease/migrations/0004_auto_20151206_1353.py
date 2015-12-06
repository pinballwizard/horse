# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import flatlease.models


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0003_auto_20151122_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='client',
            name='health',
            field=models.CharField(max_length=50, choices=[('Здоров', 'Здоров'), ('Серьезные проблемы со здоровьем', 'Серьезные проблемы со здоровьем'), ('На учете в наркодиспансере', 'На учете в наркодиспансере'), ('На учете в психдиспансере', 'На учете в психдиспансере')], default='Здоров', verbose_name='Состояние здоровья'),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(default='/static/flatlease/images/userPlaceholder.png', verbose_name='Фотография', upload_to=flatlease.models.photo_file_path),
        ),
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.CharField(max_length=20, choices=[('Заявление', 'Заявление'), ('Анкета', 'Анкета'), ('Договор', 'Договор')], default='Заявление', verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='birthday',
            field=models.DateField(verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='relation',
            field=models.CharField(max_length=10, choices=[('Отец', 'Отец'), ('Мать', 'Мать'), ('Ребенок', 'Ребенок')], default='Отец', verbose_name='Родство'),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='birthday',
            field=models.DateField(verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(max_length=20, choices=[('Наличные', 'Наличные'), ('Безналичный', 'Безналичный'), ('Внутренний', 'Внутренний перевод')], default='Наличные', verbose_name='Тип платежа'),
        ),
    ]
