# Generated by Django 4.0.6 on 2022-08-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0003_goals_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='goals',
            name='pomodoro',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
