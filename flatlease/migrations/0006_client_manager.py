# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flatlease', '0005_auto_20151114_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='manager',
            field=models.ForeignKey(verbose_name='Менеджер', default='manager1', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
