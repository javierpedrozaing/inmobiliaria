# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0002_inmuebles_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmuebles',
            name='Banos',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inmuebles',
            name='cocina',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inmuebles',
            name='fondo',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inmuebles',
            name='frente',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inmuebles',
            name='habitaciones',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inmuebles',
            name='pisos',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='inmuebles',
            name='telefono',
            field=models.IntegerField(max_length=120, blank=True),
            preserve_default=True,
        ),
    ]
