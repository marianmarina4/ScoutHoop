# Generated by Django 5.0.7 on 2024-08-26 21:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0013_delete_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('year_played', models.PositiveIntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='players.player')),
            ],
        ),
    ]
