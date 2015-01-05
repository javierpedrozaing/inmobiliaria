# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmuebles',
            name='titulo',
            field=models.CharField(default=b'Inmuebe', max_length=120),
            preserve_default=True,
        ),
    ]
