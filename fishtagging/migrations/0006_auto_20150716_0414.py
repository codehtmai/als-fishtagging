# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0005_auto_20150716_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whzonecodes',
            name='zoneno',
        ),
        migrations.AddField(
            model_name='whzonecodes',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
