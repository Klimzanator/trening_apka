# Generated by Django 4.0.1 on 2022-01-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='time',
            field=models.IntegerField(),
        ),
    ]
