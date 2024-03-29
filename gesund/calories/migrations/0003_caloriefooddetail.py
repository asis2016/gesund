# Generated by Django 4.0.1 on 2022-03-24 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0002_caloriecategory_alter_calorieintake_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalorieFoodDetail',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('food', models.TextField()),
                ('description', models.TextField()),
                ('calories', models.FloatField()),
                ('protein', models.FloatField()),
                ('fat', models.FloatField()),
                ('carb', models.FloatField()),
                ('sugar', models.FloatField()),
                ('fiber', models.FloatField()),
                ('status', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calories.caloriecategory')),
            ],
        ),
    ]
