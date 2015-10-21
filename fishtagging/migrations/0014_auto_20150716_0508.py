# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0013_auto_20150716_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagtypes',
            name='lotprice',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='tagtypes',
            name='needleprice',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
    ]
