# Generated by Django 3.1.14 on 2022-02-16 14:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0019_auto_20220216_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 16, 14, 17, 32, 720749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 16, 14, 17, 32, 721449, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 16, 14, 17, 32, 719930, tzinfo=utc)),
        ),
    ]
