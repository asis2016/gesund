# Generated by Django 4.0.1 on 2022-03-24 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0003_caloriefooddetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caloriefooddetail',
            old_name='category',
            new_name='category_id',
        ),
    ]
