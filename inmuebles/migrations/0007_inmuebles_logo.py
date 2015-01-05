# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles', '0006_auto_20141208_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmuebles',
            name='logo',
            field=models.ImageField(default=b'', upload_to=b'LogoInmueble'),
            preserve_default=True,
        ),
    ]
