# Generated by Django 3.1 on 2020-09-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0013_auto_20200903_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='location',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]