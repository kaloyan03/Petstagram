# Generated by Django 4.0.4 on 2022-05-11 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_day',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='description',
        ),
    ]
