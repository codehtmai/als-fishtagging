# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0015_auto_20150716_0516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disposition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disposition', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='LandLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('legend', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Recapture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tagno', models.IntegerField(null=True, blank=True)),
                ('releaseno', models.IntegerField(null=True, blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('place', models.CharField(max_length=255, blank=True)),
                ('location', models.IntegerField(null=True, blank=True)),
                ('length', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('oz', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('weight', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('comments', models.CharField(max_length=255, blank=True)),
                ('tagged', models.CharField(max_length=255, blank=True)),
                ('un', models.CharField(max_length=255, blank=True)),
                ('undaterun', models.DateTimeField(null=True, blank=True)),
                ('wh', models.CharField(max_length=255, blank=True)),
                ('crossRefTag', models.IntegerField(null=True, blank=True)),
                ('whdaterun', models.DateTimeField(null=True, blank=True)),
                ('lat', models.CharField(max_length=255, blank=True)),
                ('long', models.CharField(max_length=255, blank=True)),
                ('disposition', models.ForeignKey(to='fishtagging.Disposition')),
                ('legend', models.ForeignKey(to='fishtagging.LandLocation')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(unique=True)),
                ('species', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('st', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Taggers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first', models.CharField(max_length=30, blank=True)),
                ('last', models.CharField(max_length=30)),
                ('suffix', models.CharField(max_length=10, blank=True)),
                ('prefix', models.CharField(max_length=10, blank=True)),
                ('nick', models.CharField(max_length=30, blank=True)),
                ('address1', models.CharField(max_length=50, blank=True)),
                ('address', models.CharField(max_length=50, blank=True)),
                ('muni', models.CharField(max_length=30, blank=True)),
                ('zip', models.CharField(max_length=10, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('phone', models.CharField(max_length=14, blank=True)),
                ('cell', models.CharField(max_length=14, blank=True)),
                ('business', models.CharField(max_length=14, blank=True)),
                ('member', models.BooleanField(default=False)),
                ('duesDueDate', models.DateTimeField(blank=True)),
                ('dateJoined', models.DateTimeField(blank=True)),
                ('clubName', models.CharField(max_length=50, blank=True)),
                ('clubMember', models.BooleanField()),
                ('starting', models.IntegerField(null=True, blank=True)),
                ('updating', models.IntegerField(null=True, blank=True)),
                ('total', models.IntegerField(null=True, blank=True)),
                ('st', models.ForeignKey(to='fishtagging.States', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TagPurchases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tagpurchaseid', models.IntegerField()),
                ('purchasedate', models.DateTimeField()),
                ('tagstart', models.IntegerField()),
                ('tagend', models.IntegerField()),
                ('numberOfKits', models.IntegerField(null=True, blank=True)),
                ('numberOfNeedles', models.IntegerField(null=True, blank=True)),
                ('purchaseAmount', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('postageHandling', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('newMember', models.BooleanField(default=True)),
                ('comment', models.CharField(max_length=200, blank=True)),
                ('memberName', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tagno', models.IntegerField(null=True, blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('place', models.CharField(max_length=255, blank=True)),
                ('length', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('oz', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('weight', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('wh', models.CharField(max_length=255, blank=True)),
                ('crossRefTag', models.IntegerField(null=True, blank=True)),
                ('releaseno', models.IntegerField(null=True, blank=True)),
                ('daterun', models.DateTimeField(null=True, blank=True)),
                ('lat', models.CharField(max_length=255, blank=True)),
                ('long', models.CharField(max_length=255, blank=True)),
                ('species', models.ForeignKey(to='fishtagging.Species')),
                ('tagger', models.ForeignKey(to='fishtagging.Taggers')),
            ],
            options={
                'ordering': ('tagno',),
            },
        ),
        migrations.CreateModel(
            name='TagTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typenum', models.IntegerField()),
                ('tagtype', models.CharField(max_length=12)),
                ('lotsize', models.IntegerField(null=True, blank=True)),
                ('lotprice', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('needleprice', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('start', models.IntegerField(null=True, blank=True)),
                ('end', models.IntegerField(null=True, blank=True)),
            ],
        ),
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
            model_name='tags',
            name='whzone',
            field=models.ForeignKey(to='fishtagging.WHZoneCodes'),
        ),
        migrations.AddField(
            model_name='tagpurchases',
            name='type',
            field=models.ForeignKey(to='fishtagging.TagTypes'),
        ),
        migrations.AddField(
            model_name='recapture',
            name='tagger',
            field=models.ForeignKey(to='fishtagging.Taggers'),
        ),
        migrations.AddField(
            model_name='recapture',
            name='whzone',
            field=models.ForeignKey(to='fishtagging.WHZoneCodes'),
        ),
    ]
