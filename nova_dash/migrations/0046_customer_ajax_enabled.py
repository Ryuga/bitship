# Generated by Django 3.1.4 on 2020-12-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova_dash', '0045_auto_20201223_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='ajax_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
