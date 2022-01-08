from django.contrib.auth.models import User
from django.db import models


class Master(User):

    departments = ((0, 'Комунальний сервіс'), (1, 'Сантехніка'), (2, 'Електрика'))

    is_staff = True
    staff_full_name = models.CharField(max_length=60, blank=False, default='ПІБ')

    phone = models.CharField(max_length=10, blank=False)
    department = models.IntegerField(choices=departments)

    objects = models.Manager()

    def __str__(self):
        return f'Client {self.username}'
