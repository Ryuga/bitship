# Generated by Django 3.1.4 on 2020-12-22 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nova_dash', '0044_auto_20201223_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='app',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='folder', to='nova_dash.app'),
        ),
    ]
