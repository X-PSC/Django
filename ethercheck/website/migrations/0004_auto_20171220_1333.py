# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='blockHash',
            field=models.CharField(blank=True, default=b'', max_length=64, verbose_name=b'BlockHash'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='blockNumber',
            field=models.IntegerField(default=0, verbose_name=b'BlockNumber'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='montant',
            field=models.FloatField(default=0, verbose_name=b'Value'),
        ),
    ]
