import logging

from users.models import Client, Counter

from django.db import DatabaseError

logger = logging.getLogger(__name__)


def push_counters(sender, instance: Client, created, **kwargs):
    if created:
        try:
            instance.create_water_counter()
            logger.info('create_water_counter() success')
        except (DatabaseError, Exception) as exception:
            Counter.objects.get_or_create(client=instance, type=Counter.Type.WATER)
            logger.error(f'create_water_counter() failed, exception ({exception})')
            instance.save()

        try:
            instance.create_electricity_counter()
            logger.info('create_electricity_counter() success')
        except (DatabaseError, Exception) as exception:
            Counter.objects.get_or_create(client=instance, type=Counter.Type.ELECTRICITY)
            logger.error(f'create_electricity_counter() failed, exception ({exception})')
            instance.save()
