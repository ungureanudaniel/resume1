# Generated by Django 3.1.14 on 2022-02-15 09:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0012_auto_20220215_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 15, 9, 16, 3, 971907, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 15, 9, 16, 3, 972532, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 15, 9, 16, 3, 971072, tzinfo=utc)),
        ),
    ]
