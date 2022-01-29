import uuid

from django.db.models import F
from django.utils.timezone import now
from bd_service import settings

from django.db import models
from django.contrib.auth.models import User
import requests

__all__ = 'Account', 'Client', 'Counter', 'Metric', 'Task', 'Transaction'


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
    datetime = models.DateTimeField(default=now)
    type = models.IntegerField(choices=Type.CHOICES)
    value = models.CharField(max_length=10, default=0)

    objects = models.Manager()

    def __str__(self):
        return f'Counter {self.id}'

    class Meta:
        verbose_name = 'Лічильник'
        verbose_name_plural = 'Лічильники'


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
    type = models.IntegerField(choices=Type.CHOICES)
    is_active = models.BooleanField(default=False)

    @property
    def type_description(self):
        if self.type == 0:
            return 'Комунальний сервіс'
        elif self.type == 1:
            return 'Водопостачання'
        elif self.type == 2:
            return 'Електроенергія'

    @property
    def type_href(self):
        if self.type == 0:
            return 'building-service'
        elif self.type == 1:
            return 'water'
        elif self.type == 2:
            return 'electricity'

    contract = models.CharField(max_length=10, default=0)
    number = models.CharField(max_length=9, default=0)
    traffic = models.CharField(max_length=10, default=0)
    requisites = models.CharField(max_length=29, default=0)
    payment_target = models.CharField(max_length=30, default=0)

    objects = models.Manager()

    def __str__(self):
        return f'Account {self.id}'

    class Meta:
        verbose_name = 'Рахунок'
        verbose_name_plural = 'Рахунки'


class Client(User):

    client_full_name = models.CharField(max_length=60, blank=False, default='ПІБ')

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

    def create_accounts(self):
        communal_service_account_data = requests.get(settings.external_url['communal_service_account']).json()
        if communal_service_account_data:
            Account.objects.get_or_create(
                client=self,
                balance=communal_service_account_data['balance'],
                type=Account.Type.COMMUNAL_SERVICE,
                is_active=self.communal_service
            )

        water_account_data = requests.get(settings.external_url['water_account']).json()
        if water_account_data:
            Account.objects.get_or_create(
                client=self,
                balance=water_account_data['balance'],
                type=Account.Type.WATER,
                is_active=self.water
            )

        electricity_account_data = requests.get(settings.external_url['electricity_account']).json()
        if electricity_account_data:
            Account.objects.get_or_create(
                client=self,
                balance=electricity_account_data['balance'],
                type=Account.Type.ELECTRICITY,
                is_active=self.electricity
            )

    def create_counters(self):
        water_counter_data = requests.get(settings.external_url['water_counter']).json()
        if water_counter_data:
            Counter.objects.get_or_create(
                client=self,
                datetime=water_counter_data['datetime'],
                type=Counter.Type.WATER,
                value=water_counter_data['value']
            )

        electricity_counter_data = requests.get(settings.external_url['electricity_counter']).json()
        if electricity_counter_data:
            Counter.objects.get_or_create(
                client=self,
                datetime=electricity_counter_data['datetime'],
                type=Counter.Type.ELECTRICITY,
                value=electricity_counter_data['value']
            )

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

    objects = models.Manager()

    def __str__(self):
        return f'Client {self.username}'

    class Meta:
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'


class Transaction(models.Model):

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

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

    class Status:
        UNDEFINED = 0
        PENDING = 1
        SUCCESS = 2
        FAILED = 3

        CHOICES = [
            (UNDEFINED, 'Не визначено'),
            (PENDING, 'В обробці'),
            (SUCCESS, 'Успішно'),
            (FAILED, 'Забраковано'),
        ]

        _default_value, _name = CHOICES[0]

    date = models.DateField()
    time = models.TimeField()
    client = models.ForeignKey('Client', models.DO_NOTHING)
    type = models.IntegerField(choices=Type.CHOICES)
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=False)
    appointment = models.IntegerField(choices=Appointment.CHOICES)
    status = models.IntegerField(choices=Status.CHOICES, null=True)

    @property
    def type_description(self):
        if self.type == 0:
            return 'Нарахування'
        elif self.type == 1:
            return 'Оплата'

    @property
    def status_description(self):
        if self.status == 0:
            return 'Не визначено'
        elif self.status == 1:
            return 'В обробці'
        elif self.status == 2:
            return 'Успішно'
        elif self.status == 3:
            return 'Забраковано'

    def create_transaction(self):
        if self.type == Transaction.Type.CREDIT:
            Account.objects.filter(client=self.client, type=self.appointment).update(balance=F('balance') + self.amount)
            self.status = self.Status.SUCCESS
        elif self.type == Transaction.Type.DEBIT:
            Account.objects.filter(client=self.client, type=self.appointment).update(balance=F('balance') - self.amount)
            self.status = self.Status.SUCCESS
        else:
            raise NotImplementedError(f'Transaction type {self.type} not implemented')
        self.save()

    objects = models.Manager()

    def __str__(self):
        return f'Transaction {self.id}'

    class Meta:
        verbose_name = 'Транзакція'
        verbose_name_plural = 'Транзакції'


class Metric(models.Model):

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Appointment:
        WATER = 1
        ELECTRICITY = 2

        CHOICES = [
            (WATER, 'Водопостачання'),
            (ELECTRICITY, 'Електропостачання'),
        ]

        _default_value, _name = CHOICES[0]

    date = models.DateField(default=now)
    client = models.ForeignKey('Client', models.DO_NOTHING)
    value = models.CharField(max_length=10, default=0)
    appointment = models.IntegerField(choices=Appointment.CHOICES)

    def create_metric(self):
        Counter.objects.filter(client=self.client, type=self.appointment).update(value=self.value)
        self.save()

    objects = models.Manager()

    def __str__(self):
        return f'Metric {self.id}'

    class Meta:
        verbose_name = 'Показники лічильника'
        verbose_name_plural = 'Показники лічильників'


class Task(models.Model):

    statuses = ((0, 'Нова заявка'), (1, 'Передано в роботу'), (2, 'Взято в роботу'), (3, 'Виконано'))
    appointments = ((0, 'Комунальний сервіс'), (1, 'Сантехніка'), (2, 'Електрика'))

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    client = models.ForeignKey(Client, models.DO_NOTHING)
    datetime = models.DateTimeField(default=now)
    text = models.TextField()
    status = models.IntegerField(choices=statuses)
    appointment = models.IntegerField(choices=appointments)

    @property
    def status_description(self):
        if self.status == 0:
            return 'Нова заявка'
        elif self.status == 1:
            return 'Передано в роботу'
        elif self.status == 2:
            return 'Взято в роботу'
        elif self.status == 3:
            return 'Виконано'

    @property
    def appointment_description(self):
        if self.appointment == 0:
            return 'Комунальний сервіс'
        elif self.appointment == 1:
            return 'Сантехніка'
        elif self.appointment == 2:
            return 'Електрика'

    objects = models.Manager()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
