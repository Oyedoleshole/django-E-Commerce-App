# Generated by Django 3.2.4 on 2022-12-05 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0011_alter_messagemodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
