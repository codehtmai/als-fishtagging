# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0018_auto_20150716_0620'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueFish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('species', models.ForeignKey(to='fishtagging.Species')),
            ],
        ),
        migrations.AddField(
            model_name='tags',
            name='comments',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='tags',
            name='disposition',
            field=models.ForeignKey(default=9, to='fishtagging.Disposition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tags',
            name='isRecapture',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tags',
            name='location',
            field=models.ForeignKey(default=0, to='fishtagging.LandLocation'),
            preserve_default=False,
        ),
    ]
