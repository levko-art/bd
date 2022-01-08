# Generated by Django 3.2.9 on 2022-01-08 13:27

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_counter_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 8, 15, 27, 2, 695893)),
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('value', models.CharField(default=0, max_length=10)),
                ('appointment', models.IntegerField(choices=[(1, 'Водопостачання'), (2, 'Електропостачання')])),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.client')),
            ],
        ),
    ]
