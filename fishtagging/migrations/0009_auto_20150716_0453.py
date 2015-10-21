# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0008_auto_20150716_0450'),
    ]

    operations = [
        migrations.CreateModel(
            name='WHZoneCodes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zoneno', models.CharField(max_length=5)),
                ('masterzone', models.CharField(max_length=2, blank=True)),
                ('description', models.CharField(max_length=80, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='recapture',
            name='whzone',
            field=models.ForeignKey(default=1, to='fishtagging.WHZoneCodes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tags',
            name='whzone',
            field=models.ForeignKey(default=1, to='fishtagging.WHZoneCodes'),
            preserve_default=False,
        ),
    ]
