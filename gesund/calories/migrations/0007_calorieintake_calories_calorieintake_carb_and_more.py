# Generated by Django 4.0.1 on 2022-06-03 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0006_calorieintake_author_calorieintake_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='calorieintake',
            name='calories',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calorieintake',
            name='carb',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calorieintake',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calorieintake',
            name='fat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calorieintake',
            name='fiber',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calorieintake',
            name='food_detail_ref',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calorieintake',
            name='protein',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calorieintake',
            name='sugar',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='calorieintake',
            name='food',
            field=models.TextField(blank=True, null=True),
        ),
    ]
