# Generated by Django 4.0.1 on 2022-03-20 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoros', '0002_pomodoro_author_pomodoro_pomodoro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pomodoro',
            name='author',
        ),
    ]
