# Generated by Django 3.1.7 on 2021-04-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova_dash', '0086_auto_20210406_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='last_deployment_status',
            field=models.CharField(choices=[('bg-success', 'success'), ('bg-danger', 'failed'), ('bg-warning', 'pending'), ('bg-dark', 'rejected'), ('bg-secondary', 'Not deployed')], default='Not deployed', max_length=20),
        ),
    ]
