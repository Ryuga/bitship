# Generated by Django 3.1.5 on 2021-02-26 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nova_dash', '0065_auto_20210226_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='nova_dash.customer'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('bg-danger', 'Failed'), ('bg-dark', 'Canceled'), ('bg-warning', 'Pending'), ('bg-success', 'Success')], max_length=15),
        ),
    ]
