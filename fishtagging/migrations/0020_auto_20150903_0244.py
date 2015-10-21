# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0019_auto_20150902_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggers',
            name='taggersMasterID',
            field=models.IntegerField(blank=True),
        ),
    ]
