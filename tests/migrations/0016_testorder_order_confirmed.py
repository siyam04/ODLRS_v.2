# Generated by Django 2.2.1 on 2019-07-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0015_testorder_validation'),
    ]

    operations = [
        migrations.AddField(
            model_name='testorder',
            name='order_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
