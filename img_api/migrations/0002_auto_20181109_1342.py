# Generated by Django 2.1.3 on 2018-11-09 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshots',
            name='coordinates',
            field=models.TextField(default=None, max_length=1024),
        ),
        migrations.AlterField(
            model_name='screenshots',
            name='created',
            field=models.DateTimeField(default=None),
        ),
    ]
