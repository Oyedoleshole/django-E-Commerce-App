# Generated by Django 3.2.4 on 2022-12-15 07:30

from django.db import migrations
import user_login_with_otp.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login_with_otp', '0003_alter_profile_id'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='profile',
            managers=[
                ('objects', user_login_with_otp.models.Another_user_method()),
            ],
        ),
    ]
