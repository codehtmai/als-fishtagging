# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0007_auto_20150716_0415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recapture',
            name='whzone',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='whzone',
        ),
        migrations.DeleteModel(
            name='WHZoneCodes',
        ),
    ]
