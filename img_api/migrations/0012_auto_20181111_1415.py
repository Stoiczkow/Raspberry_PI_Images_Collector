# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-11-11 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_api', '0011_auto_20181110_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screenshots',
            name='coordinates',
        ),
        migrations.AddField(
            model_name='screenshots',
            name='latitude',
            field=models.TextField(default=None, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='screenshots',
            name='longitude',
            field=models.TextField(default=None, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='screenshots',
            name='created',
            field=models.TextField(default=None, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='screenshots',
            name='img',
            field=models.ImageField(blank=True, upload_to='image_collector/static/img_api'),
        ),
    ]
