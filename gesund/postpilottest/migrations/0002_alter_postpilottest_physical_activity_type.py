# Generated by Django 4.0.6 on 2022-07-18 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postpilottest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpilottest',
            name='physical_activity_type',
            field=models.TextField(help_text='During the experiment period, what type of physical activities did you perform?'),
        ),
    ]
