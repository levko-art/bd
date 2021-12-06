from django.apps import AppConfig
from django.db.models.signals import post_save


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = "Blockfarm"

    def ready(self):
        import users.signals
        from users.models import Client

        post_save.connect(users.signals.push_counters, sender=Client, dispatch_uid='push_counters')
