# Generated by Django 4.0.6 on 2022-07-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoros', '0008_alter_pomodoro_datestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pomodoro',
            name='timestamp',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pomodoro',
            name='datestamp',
            field=models.DateField(auto_now=True),
        ),
    ]
