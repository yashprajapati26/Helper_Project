# Generated by Django 4.1 on 2022-08-15 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helper_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='mpoly',
            new_name='data',
        ),
    ]