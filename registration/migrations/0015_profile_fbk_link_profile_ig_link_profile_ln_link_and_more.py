# Generated by Django 5.0.7 on 2024-08-29 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_remove_profile_link_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fbk_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='ig_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='ln_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='x_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
