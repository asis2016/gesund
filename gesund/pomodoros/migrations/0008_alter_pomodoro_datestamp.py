# Generated by Django 4.0.6 on 2022-07-17 16:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoros', '0007_remove_pomodoro_datetimestamp_pomodoro_datestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pomodoro',
            name='datestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 7, 17, 16, 21, 31, 381455, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
