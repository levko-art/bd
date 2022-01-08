from django.apps import AppConfig
from django.db.models.signals import post_save


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = "bd_service"

    def ready(self):
        import users.signals
        from users.models import Client
        from users.models import Transaction

        post_save.connect(users.signals.push_counters, sender=Client, dispatch_uid='push_counters')
        post_save.connect(users.signals.push_accounts, sender=Client, dispatch_uid='push_accounts')
        post_save.connect(users.signals.push_transactions, sender=Transaction, dispatch_uid='push_transactions')
