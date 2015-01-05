# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField(max_length=255)),
                ('id_rol', models.ForeignKey(related_name='id_roles', to='roles.Rol', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
