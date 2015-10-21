# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0016_auto_20150716_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='taggers',
            name='taggersMasterID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
