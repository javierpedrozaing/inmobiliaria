# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0004_auto_20141208_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmuebles',
            name='telefono',
            field=models.IntegerField(max_length=120, null=True, blank=True),
            preserve_default=True,
        ),
    ]
