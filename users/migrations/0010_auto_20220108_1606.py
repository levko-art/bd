# Generated by Django 3.2.9 on 2022-01-08 14:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20220108_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='metric',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]