# Generated by Django 2.2.1 on 2019-06-22 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic_centers', '0006_auto_20190620_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosticstaff',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
