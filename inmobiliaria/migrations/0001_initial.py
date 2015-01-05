# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inmobiliaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('direccon', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
