# Generated by Django 2.2.1 on 2019-05-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic_centers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosticcenter',
            name='website',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='diagnosticcenter',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
