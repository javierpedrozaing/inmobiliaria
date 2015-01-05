# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(blank=True)),
                ('fotoNombre', models.ImageField(upload_to=b'fotosInmueble')),
                ('fotoType', models.CharField(max_length=255)),
                ('fotoSize', models.PositiveIntegerField()),
                ('fotoUpdate', models.DateField()),
                ('id_inmueble', models.ForeignKey(to='inmuebles.Inmuebles')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
