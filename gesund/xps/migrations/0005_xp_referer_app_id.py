# Generated by Django 4.0.6 on 2022-08-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xps', '0004_alter_xp_datestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='xp',
            name='referer_app_id',
            field=models.TextField(blank=True, null=True),
        ),
    ]