# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0009_auto_20150716_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagtypes',
            name='lotsize',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
