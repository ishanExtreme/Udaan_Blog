# Generated by Django 3.0.3 on 2020-04-03 11:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0017_auto_20200402_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 11, 3, 59, 568448, tzinfo=utc)),
        ),
    ]
