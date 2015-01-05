# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmobiliaria',
            name='telefono',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
