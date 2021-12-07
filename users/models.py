import datetime
import uuid

from BD_service import settings

from django.db.models import F
from django.db import models, transaction
from django.contrib.auth.models import User
import requests


__all__ = 'Client', 'Counter', 'Account', 'Transaction'


class Counter(models.Model):

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Type:
        WATER = 0
        ELECTRICITY = 1

        CHOICES = [
            (WATER, 'Водопостачання'),
            (ELECTRICITY, 'Електроенергія'),
        ]

        _default_value, _name = CHOICES[0]

    client = models.ForeignKey('Client', models.PROTECT)
    datetime = models.DateTimeField(default=datetime.datetime.now())
    type = models.IntegerField(choices=Type.CHOICES)
    value = models.CharField(max_length=10, default=0)

    objects = models.Manager()

    def __str__(self):
        return f'Counter {self.id}'


class Account(models.Model):

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Type:
        COMMUNAL_SERVICE = 0
        WATER = 1
        ELECTRICITY = 2

        CHOICES = [
            (COMMUNAL_SERVICE, 'Комунальний сервіс'),
            (WATER, 'Водопостачання'),
            (ELECTRICITY, 'Електроенергія'),
        ]

        _default_value, _name = CHOICES[0]

    client = models.ForeignKey('Client', models.PROTECT)
    balance = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    objects = models.Manager()

    def __str__(self):
        return f'Account {self.id}'


class Client(User):

    id = models.CharField(max_length=9, blank=False)

    phone = models.CharField(max_length=10, blank=False)
    viber = models.BooleanField(default=False)
    telegram = models.BooleanField(default=False)
    reserve_phone = models.CharField(max_length=10, blank=True)

    housing_complex = models.CharField(max_length=20, blank=False)
    region = models.CharField(max_length=15, blank=False)
    district = models.CharField(max_length=25, blank=False)
    town = models.CharField(max_length=30, blank=False)
    street = models.CharField(max_length=20, blank=False)
    building = models.IntegerField(blank=False)
    house_building = models.IntegerField(blank=True)
    flat = models.IntegerField(blank=False)

    communal_service = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)

    @property
    def communal_service_account(self) -> Account:
        return Account.objects.get(type=Account.Type.COMMUNAL_SERVICE, client=self)

    @property
    def water_account(self) -> Account:
        return Account.objects.get(type=Account.Type.WATER, client=self)

    @property
    def electricity_account(self) -> Account:
        return Account.objects.get(type=Account.Type.ELECTRICITY, client=self)

    @property
    def water_counter(self) -> Counter:
        return Counter.objects.get(type=Counter.Type.WATER, client=self)

    @property
    def electricity_counter(self) -> Counter:
        return Counter.objects.get(type=Counter.Type.ELECTRICITY, client=self)

    def create_accounts(self):
        communal_service_account_data = requests.get(settings.external_url['communal_service_account']).json()
        water_account_data = requests.get(settings.external_url['water_account']).json()
        electricity_account_data = requests.get(settings.external_url['electricity_account']).json()
        with transaction.atomic():
            Account.objects.get_or_create(
                type=Account.Type.COMMUNAL_SERVICE,
                client=self,
                balance=communal_service_account_data['balance']
            )
            Account.objects.get_or_create(
                type=Account.Type.WATER,
                client=self,
                balance=water_account_data['balance']
            )
            Account.objects.get_or_create(
                type=Account.Type.ELECTRICITY,
                client=self,
                balance=electricity_account_data['balance']
            )

    def create_counters(self):
        water_counter_data = requests.get(settings.external_url['water_counter']).json()
        electricity_counter_data = requests.get(settings.external_url['electricity_counter']).json()
        with transaction.atomic():
            Counter.objects.get_or_create(
                client=self,
                datetime=water_counter_data['datetime'],
                type=Counter.Type.WATER,
                value=water_counter_data['value']
            )
            Counter.objects.get_or_create(
                client=self,
                datetime=electricity_counter_data['datetime'],
                type=Counter.Type.WATER,
                value=electricity_counter_data['value']
            )

    objects = models.Manager()

    def __str__(self):
        return f'Client {self.username}'


class Transaction(models.Model):

    class Type:
        DEBIT = 0
        CREDIT = 1

        CHOICES = [
            (DEBIT, 'Нарахування'),
            (CREDIT, 'Оплата'),
        ]

        _default_value, _name = CHOICES[0]

    class Appointment:
        COMMUNAL_SERVICE = 0
        WATER = 1
        ELECTRICITY = 2

        CHOICES = [
            (COMMUNAL_SERVICE, 'Комунальний сервіс'),
            (WATER, 'Водопостачання'),
            (ELECTRICITY, 'Електропостачання'),
        ]

        _default_value, _name = CHOICES[0]

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    date = models.DateField()
    time = models.TimeField()
    client = models.ForeignKey('Client', models.DO_NOTHING)
    type = models.IntegerField(choices=Type.CHOICES)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False)
    appointment = models.IntegerField(choices=Appointment.CHOICES)

    def create_transaction(self):
        if self.type == Transaction.Type.CREDIT:
            Account.objects.filter(client=self.client, type=self.type).update(balance=F('balance') + self.amount)
        elif self.type == Transaction.Type.DEBIT:
            Account.objects.filter(client=self.client, type=self.type).update(balance=F('balance') - self.amount)
        else:
            raise NotImplementedError(f'Transaction type {self.type} not implemented')
        self.save()

    objects = models.Manager()

    def __str__(self):
        return f'Transaction {self.id}'


# class Task(models.Model):
#
#     types = ((0, 'Нова заявка'), (1, 'Передано в роботу'), (2, 'Взято в роботу'), (3, 'Виконано'))
#
#     client = models.ForeignKey(Client, models.DO_NOTHING, related_name='TASK_client')
#     datetime = models.DateTimeField()
#     text = models.TextField()
#     status = models.IntegerField(choices=types)
#
#     def __str__(self):
#         return self.id
