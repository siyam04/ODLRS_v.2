# Generated by Django 2.2.1 on 2019-06-22 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0003_profile_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]
