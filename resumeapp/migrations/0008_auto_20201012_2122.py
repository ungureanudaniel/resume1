# Generated by Django 3.1 on 2020-10-12 21:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0007_auto_20201012_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 12, 21, 22, 5, 431450)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 12, 21, 22, 5, 432036)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 12, 21, 22, 5, 430651)),
        ),
    ]
