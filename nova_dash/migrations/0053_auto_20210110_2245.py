# Generated by Django 3.1.5 on 2021-01-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova_dash', '0052_app_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='config',
            field=models.JSONField(default=dict),
        ),
    ]
