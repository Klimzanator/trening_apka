# Generated by Django 4.0.1 on 2022-01-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_alter_training_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='time',
            field=models.FloatField(),
        ),
    ]
