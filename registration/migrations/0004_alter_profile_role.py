# Generated by Django 5.0.7 on 2024-08-23 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_remove_profile_is_agent_remove_profile_is_player_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Agent', 'Agente'), ('Player', 'Jugador')], max_length=10),
        ),
    ]
