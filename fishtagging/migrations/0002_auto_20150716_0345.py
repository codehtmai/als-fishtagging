# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishtagging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recapture',
            name='crossRefTag',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recapture',
            name='date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recapture',
            name='length',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='recapture',
            name='location',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recapture',
            name='oz',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='recapture',
            name='releaseno',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recapture',
            name='tagno',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recapture',
            name='undaterun',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recapture',
            name='weight',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='recapture',
            name='whdaterun',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taggers',
            name='starting',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taggers',
            name='total',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taggers',
            name='updating',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tagpurchases',
            name='numberOfKits',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tagpurchases',
            name='numberOfNeedles',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tagpurchases',
            name='postageHandling',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='tagpurchases',
            name='purchaseAmount',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='crossRefTag',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='daterun',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='length',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='oz',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='releaseno',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='tagno',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='weight',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='tagtypes',
            name='end',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tagtypes',
            name='lotprice',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='tagtypes',
            name='lotsize',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tagtypes',
            name='needleprice',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='tagtypes',
            name='start',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
