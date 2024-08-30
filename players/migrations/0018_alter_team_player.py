# Generated by Django 5.0.7 on 2024-08-27 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0017_remove_player_teams_team_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='player',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='players.player'),
        ),
    ]
