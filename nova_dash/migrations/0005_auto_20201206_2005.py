# Generated by Django 3.1.4 on 2020-12-06 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova_dash', '0004_customer_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
