# Generated by Django 5.0.7 on 2024-08-24 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_alter_profile_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
