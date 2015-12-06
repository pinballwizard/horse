# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatlease', '0006_auto_20151206_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixedproperty',
            name='build_year',
            field=models.DateField(verbose_name='Дата постройки'),
        ),
    ]
