# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0002_relative_relation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passport',
            old_name='data',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='client',
            name='health',
            field=models.CharField(choices=[('healthy', 'Здоров'), ('sick', 'Серьезные проблемы со здоровьем'), ('addict', 'На учете в наркодиспансере'), ('psycho', 'На учете в психдиспансере')], max_length=50, verbose_name='Состояние здоровья', default='healthy'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='relation',
            field=models.CharField(choices=[('father', 'Отец'), ('mother', 'Мать'), ('child', 'Ребенок')], max_length=10, verbose_name='Родство', default='father'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('cash', 'Наличные'), ('cashless', 'Безналичный'), ('inside', 'Внутренний перевод')], max_length=20, verbose_name='Тип платежа', default='cash'),
        ),
    ]
