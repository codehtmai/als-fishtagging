# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0014_auto_20150716_0508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recapture',
            name='disposition',
        ),
        migrations.RemoveField(
            model_name='recapture',
            name='legend',
        ),
        migrations.RemoveField(
            model_name='recapture',
            name='tagger',
        ),
        migrations.RemoveField(
            model_name='recapture',
            name='whzone',
        ),
        migrations.RemoveField(
            model_name='taggers',
            name='st',
        ),
        migrations.RemoveField(
            model_name='tagpurchases',
            name='type',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='species',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='tagger',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='whzone',
        ),
        migrations.DeleteModel(
            name='Disposition',
        ),
        migrations.DeleteModel(
            name='LandLocation',
        ),
        migrations.DeleteModel(
            name='Recapture',
        ),
        migrations.DeleteModel(
            name='Species',
        ),
        migrations.DeleteModel(
            name='States',
        ),
        migrations.DeleteModel(
            name='Taggers',
        ),
        migrations.DeleteModel(
            name='TagPurchases',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.DeleteModel(
            name='TagTypes',
        ),
        migrations.DeleteModel(
            name='WHZoneCodes',
        ),
    ]
