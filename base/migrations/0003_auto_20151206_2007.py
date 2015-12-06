# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20151206_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='birthday',
            field=models.DateField(verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='birthday',
            field=models.DateField(verbose_name='День рождения'),
        ),
    ]
