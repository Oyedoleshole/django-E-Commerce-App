# Generated by Django 3.2.4 on 2022-12-05 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0022_alter_messagemodel_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MessageModel',
        ),
    ]