# Generated by Django 3.2.4 on 2022-11-21 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_alter_uploadimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimages',
            name='image',
            field=models.ImageField(default='', max_length=255, upload_to='media/images'),
        ),
    ]
