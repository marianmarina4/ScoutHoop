# Generated by Django 5.0.7 on 2024-08-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_team_player_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='country',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='team',
            name='year',
            field=models.IntegerField(default=None),
        ),
    ]
