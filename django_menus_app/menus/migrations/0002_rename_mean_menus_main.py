# Generated by Django 4.1.1 on 2022-09-12 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menus',
            old_name='mean',
            new_name='main',
        ),
    ]
