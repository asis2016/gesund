# Generated by Django 4.0.1 on 2022-05-24 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_rename_calories_goal_goals_calories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goals',
            name='weight',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
