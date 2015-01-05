# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0003_auto_20141208_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmuebles',
            name='Banos',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inmuebles',
            name='cocina',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inmuebles',
            name='fondo',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inmuebles',
            name='frente',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inmuebles',
            name='habitaciones',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inmuebles',
            name='pisos',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
