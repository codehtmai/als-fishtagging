# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0006_auto_20150716_0414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whzonecodes',
            name='id',
        ),
        migrations.AddField(
            model_name='whzonecodes',
            name='primary',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
        ),
    ]
