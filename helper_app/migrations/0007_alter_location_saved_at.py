# Generated by Django 4.1 on 2022-08-16 04:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper_app', '0006_location_saved_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='saved_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]