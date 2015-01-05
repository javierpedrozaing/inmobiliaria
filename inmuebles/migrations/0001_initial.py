# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipoInmueble', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inmuebles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.IntegerField()),
                ('direccion', models.CharField(max_length=120)),
                ('telefono', models.IntegerField(max_length=20)),
                ('habitaciones', models.IntegerField()),
                ('parqueadero', models.NullBooleanField()),
                ('Banos', models.IntegerField()),
                ('pisos', models.IntegerField()),
                ('frente', models.IntegerField()),
                ('fondo', models.IntegerField()),
                ('cocina', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('estado', models.TextField()),
                ('id_tipoInmueble', models.ForeignKey(related_name='id_tipo', to='tipoInmueble.tipoInmueble', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
