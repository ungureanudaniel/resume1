# Generated by Django 3.1.14 on 2023-05-12 14:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0023_auto_20220627_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvfile',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 12, 14, 4, 37, 407435, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='education',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 12, 14, 4, 37, 403873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 12, 14, 4, 37, 404523, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 12, 14, 4, 37, 403115, tzinfo=utc)),
        ),
    ]