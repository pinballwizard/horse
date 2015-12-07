# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relative',
            name='relation',
            field=models.CharField(choices=[('father', 'Отец'), ('mother', 'Мать'), ('child', 'Ребенок')], verbose_name='Отношение', max_length=10, default='father'),
        ),
    ]
