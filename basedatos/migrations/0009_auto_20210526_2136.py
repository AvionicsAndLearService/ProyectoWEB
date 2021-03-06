# Generated by Django 3.0.7 on 2021-05-27 02:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basedatos', '0008_auto_20210526_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='ot',
            name='hangar',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ot',
            name='observacion',
            field=models.TextField(default=django.utils.timezone.now, max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ot',
            name='orden_ALS',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
