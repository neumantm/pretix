# Generated by Django 2.2.1 on 2019-07-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0125_voucher_show_hidden_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='show_quota_left',
            field=models.BooleanField(null=True, blank=True),
        ),
    ]
