# Generated by Django 3.1.4 on 2020-12-20 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nova_dash', '0039_remove_folder_contents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nova_dash.folder'),
        ),
    ]
