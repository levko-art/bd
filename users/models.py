from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=40)
    personal_number = models.CharField(max_length=9)

    # Contact information
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    viber = models.BooleanField(default=False)
    telegram = models.BooleanField(default=False)
    reserve_phone = models.CharField(max_length=10)

    # Address
    housing_complex = models.CharField(max_length=15)
    region = models.CharField(max_length=10)
    district = models.CharField(max_length=20)
    town = models.CharField(max_length=25)
    street = models.CharField(max_length=20)
    building = models.IntegerField()
    house_building = models.IntegerField()
    flat = models.IntegerField()

    # Services
    communal_service = models.BooleanField(default=False)
    communal_service_balance = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    water = models.BooleanField(default=False)
    water_balance = models.BooleanField(default=0)
    water_counter = models.IntegerField(default=0)

    electricity = models.BooleanField(default=False)
    electricity_balance = models.BooleanField(default=0)
    electricity_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Transaction(models.Model):

    transaction_date = models.DateField()
    transaction_time = models.TimeField()
    transaction_client = models.ForeignKey(Client, models.DO_NOTHING, related_name='TRANSACTION_client')
    transaction_type = models.BooleanField(default=False)
    transaction_sum = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False)

    def __str__(self):
        return self.id


class Counter(models.Model):

    types = ((0, 'Водопостачання'), (1, 'Електроенергія'))

    client = models.ForeignKey(Client, models.DO_NOTHING, related_name='COUNTER_client')
    datetime = models.DateTimeField()
    counter_type = models.IntegerField(choices=types)
    counter_value = models.IntegerField()

    def __str__(self):
        return self.id


class Task(models.Model):

    types = ((0, 'Нова заявка'), (1, 'Передано в роботу'), (2, 'Взято в роботу'), (3, 'Виконано'))

    client = models.ForeignKey(Client, models.DO_NOTHING, related_name='TASK_client')
    datetime = models.DateTimeField()
    text = models.TextField()
    status = models.IntegerField(choices=types)

    def __str__(self):
        return self.id
