import logging

from users.models import Account, Client, Counter, Transaction

from django.db import DatabaseError

logger = logging.getLogger(__name__)


def push_counters(sender, instance: Client, created, **kwargs):
    if created:
        try:
            instance.create_counters()
            logger.info('create_water_counter() success')
        except (DatabaseError, Exception) as exception:
            Counter.objects.get_or_create(client=instance, type=Counter.Type.WATER)
            Counter.objects.get_or_create(client=instance, type=Counter.Type.ELECTRICITY)
            logger.error(f'create_water_counter() failed, exception ({exception})')
            instance.save()


def push_accounts(sender, instance: Client, created, **kwargs):
    if created:
        try:
            instance.create_accounts()
            logger.info('create_accounts() success')
        except (DatabaseError, Exception) as exception:
            Account.objects.get_or_create(
                client=instance,
                type=Account.Type.COMMUNAL_SERVICE,
                is_active=instance.communal_service
            )
            Account.objects.get_or_create(
                client=instance,
                type=Account.Type.WATER,
                is_active=instance.water
            )
            Account.objects.get_or_create(
                client=instance,
                type=Account.Type.ELECTRICITY,
                is_active=instance.electricity
            )
            logger.error(f'create_accounts() failed, exception ({exception})')
            instance.save()


def push_transactions(sender, instance: Transaction, created, **kwargs):
    if created:
        try:
            instance.create_transaction()
            logger.info('create_transaction() success')
        except (DatabaseError, Exception) as exception:
            logger.error(f'create_transaction() failed, exception ({exception})')
            instance.status = Transaction.Status.FAILED
            instance.save()
