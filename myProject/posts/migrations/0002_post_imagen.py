# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
