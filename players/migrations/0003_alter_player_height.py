# Generated by Django 5.0.7 on 2024-08-25 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_player_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]
