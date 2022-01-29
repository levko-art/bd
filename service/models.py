from django.contrib.auth.models import User
from django.db import models

__all__ = 'StaffPhone'


class StaffPhone(models.Model):

    phone_number = models.CharField(max_length=10)
    description = models.CharField(max_length=120)
    contact_person = models.CharField(max_length=60)

    objects = models.Manager()

    def __str__(self):
        return f'Staff phone {self.phone_number}'

    class Meta:
        verbose_name = 'Сервісний номер телефону'
        verbose_name_plural = 'Сервісні номери телефонів'
