# Generated by Django 3.0.7 on 2021-05-27 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedatos', '0009_auto_20210526_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ot',
            name='tecnico',
        ),
        migrations.AddField(
            model_name='ot',
            name='tecnicos',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ot',
            name='cliente',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ot',
            name='hangar',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ot',
            name='matricula',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ot',
            name='modelo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ot',
            name='observacion',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='ot',
            name='orden_ALS',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ot',
            name='serie',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
