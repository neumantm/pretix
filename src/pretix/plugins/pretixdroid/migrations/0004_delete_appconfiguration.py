# Generated by Django 3.0.9 on 2020-10-06 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pretixdroid', '0003_appconfiguration_squashed_0005_auto_20180106_2122'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AppConfiguration',
        ),
    ]