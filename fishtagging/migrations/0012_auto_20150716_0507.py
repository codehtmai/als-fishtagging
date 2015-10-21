# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0011_auto_20150716_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagtypes',
            name='end',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tagtypes',
            name='lotprice',
            field=models.DecimalField(default=1, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tagtypes',
            name='lotsize',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tagtypes',
            name='needleprice',
            field=models.DecimalField(default=1, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tagtypes',
            name='start',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
