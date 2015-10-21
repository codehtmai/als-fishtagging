# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0017_taggers_taggersmasterid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggers',
            name='dateJoined',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taggers',
            name='duesDueDate',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taggers',
            name='st',
            field=models.ForeignKey(blank=True, to='fishtagging.States', null=True),
        ),
    ]
