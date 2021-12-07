import logging

from users.models import Client, Counter, Account

from django.db import DatabaseError, transaction

logger = logging.getLogger(__name__)


def push_counters(sender, instance: Client, created, **kwargs):
    if created:
        try:
            instance.create_counters()
            logger.info('create_counters() success')
        except (DatabaseError, Exception) as exception:
            with transaction.atomic():
                Counter.objects.get_or_create(client=instance, type=Counter.Type.WATER)
                Counter.objects.get_or_create(client=instance, type=Counter.Type.ELECTRICITY)
            logger.error(f'create_counters() failed, exception ({exception})')
            instance.save()


def push_accounts(sender, instance: Client, created, **kwargs):
    if created:
        try:
            instance.create_accounts()
            logger.info('create_accounts() success')
        except (DatabaseError, Exception) as exception:
            with transaction.atomic():
                Account.objects.get_or_create(client=instance, type=Account.Type.WATER)
                Account.objects.get_or_create(client=instance, type=Account.Type.ELECTRICITY)
            logger.error(f'create_accounts() failed, exception ({exception})')
            instance.save()
