# Generated by Django 5.0.7 on 2024-09-16 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0028_rename_team_name_team_name_team_year_played_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='year_played',
        ),
    ]
