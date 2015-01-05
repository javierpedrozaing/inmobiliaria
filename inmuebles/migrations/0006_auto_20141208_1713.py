# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0005_auto_20141208_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmuebles',
            name='telefono',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
