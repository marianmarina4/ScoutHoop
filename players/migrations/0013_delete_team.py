# Generated by Django 5.0.7 on 2024-08-26 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0012_remove_player_team_name_team_player'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Team',
        ),
    ]
