# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contratos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaInicial', models.DateField()),
                ('fechaFinal', models.DateField()),
                ('fechaDePago', models.DateField()),
                ('fechaCreacion', models.DateField()),
                ('fechaActualizacion', models.DateField()),
                ('id_usuario', models.ForeignKey(related_name='id_usuario', to='usuarios.Usuarios', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
