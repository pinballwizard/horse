# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import flatlease.models


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0003_auto_20151109_2202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='passport',
            options={'verbose_name_plural': 'Паспорта', 'verbose_name': 'Паспорт'},
        ),
        migrations.AlterModelOptions(
            name='spouse',
            options={'verbose_name_plural': 'Супруги', 'verbose_name': 'Супруг(а)'},
        ),
        migrations.RemoveField(
            model_name='passport',
            name='id',
        ),
        migrations.AlterField(
            model_name='client',
            name='health',
            field=models.CharField(verbose_name='Состояние здоровья', default='healthy', max_length=20, choices=[('healthy', 'Здоров'), ('sick', 'Болен'), ('addict', 'Наркодиспансер'), ('psycho', 'Психодиспансер')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, upload_to=flatlease.models.content_file_path, verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=flatlease.models.content_file_path, verbose_name='Документ'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='image',
            field=models.ImageField(upload_to=flatlease.models.content_file_path, verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='owner',
            field=models.OneToOneField(primary_key=True, serialize=False, verbose_name='Клиент', to='flatlease.Client'),
        ),
    ]
