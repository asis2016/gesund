# Generated by Django 4.0.6 on 2022-07-16 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoros', '0004_remove_pomodoro_pomodoro_pomodoro_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pomodoro',
            name='break_minutes',
        ),
        migrations.RemoveField(
            model_name='pomodoro',
            name='pomodoro_minutes',
        ),
        migrations.AddField(
            model_name='pomodoro',
            name='long_break',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pomodoro',
            name='pomodoro',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pomodoro',
            name='short_break',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
