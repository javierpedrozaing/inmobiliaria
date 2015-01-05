# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipoInmueble', '0001_initial'),
        ('inmuebles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='inmueblesTipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valorVenta', models.IntegerField()),
                ('ValorArriendo', models.IntegerField()),
                ('fechaArriendo', models.DateTimeField()),
                ('fechaVenta', models.DateTimeField()),
                ('inmueble', models.ForeignKey(related_name='inmueble', to='inmuebles.Inmuebles', null=True)),
                ('tipo', models.ForeignKey(related_name='tipo', to='tipoInmueble.tipoInmueble', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
