# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0002_auto_20150716_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whzonecodes',
            name='masterzone',
            field=models.CharField(max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='whzonecodes',
            name='zoneno',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
