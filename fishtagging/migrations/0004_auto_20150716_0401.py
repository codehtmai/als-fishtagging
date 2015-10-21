# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0003_auto_20150716_0356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whzonecodes',
            name='zoneno',
        ),
        migrations.AddField(
            model_name='whzonecodes',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=datetime.datetime(2015, 7, 16, 4, 1, 55, 291358, tzinfo=utc), serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
