# Generated by Django 3.1 on 2020-09-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0024_auto_20200907_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentwork',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]