# Generated by Django 3.2.4 on 2022-12-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0023_delete_messagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField(null=True)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]