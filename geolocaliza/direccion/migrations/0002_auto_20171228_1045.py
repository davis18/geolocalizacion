# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-28 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion',
            name='urbanizacion',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='direccion',
            name='via',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]