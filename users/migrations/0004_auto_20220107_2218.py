# Generated by Django 3.2.9 on 2022-01-07 20:18

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220106_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 7, 22, 18, 15, 298837)),
        ),
        migrations.AlterField(
            model_name='task',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]