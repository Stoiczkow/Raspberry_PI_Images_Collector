# Generated by Django 2.1.3 on 2018-11-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_api', '0003_auto_20181109_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshots',
            name='img',
            field=models.FileField(blank=True, upload_to='img_api/static/'),
        ),
    ]