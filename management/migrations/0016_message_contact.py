# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_auto_20170709_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.Contact'),
        ),
    ]
