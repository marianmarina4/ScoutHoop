# Generated by Django 5.0.7 on 2024-08-24 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='weight',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=5),
        ),
    ]
