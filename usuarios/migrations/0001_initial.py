# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombres', models.CharField(max_length=255)),
                ('Apellidos', models.CharField(max_length=255)),
                ('nombreUsuario', models.CharField(max_length=255)),
                ('password', models.TextField(max_length=255)),
                ('telefono', models.IntegerField()),
                ('direccion', models.TextField()),
                ('email', models.EmailField(max_length=75)),
                ('id_rol', models.ForeignKey(related_name='id_rol', to='roles.Rol', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
