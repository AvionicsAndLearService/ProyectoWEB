# Generated by Django 3.0.7 on 2021-05-27 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ot',
            name='accion',
            field=models.TextField(max_length=50000),
        ),
        migrations.AlterField(
            model_name='ot',
            name='reporte',
            field=models.TextField(max_length=5000),
        ),
    ]
