# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0012_auto_20150716_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagtypes',
            name='end',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tagtypes',
            name='lotsize',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tagtypes',
            name='start',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
