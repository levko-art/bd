from django.apps import AppConfig
from django.db.models.signals import post_save


class ApiConfig(AppConfig):
    name = 'api'
    verbose_name = "bd_service"

    def ready(self):
        import api.signals
        from users.models import Client
        from users.models import Transaction

        post_save.connect(api.signals.push_counters, sender=Client, dispatch_uid='push_counters')
        post_save.connect(api.signals.push_accounts, sender=Client, dispatch_uid='push_accounts')
        post_save.connect(api.signals.push_transactions, sender=Transaction, dispatch_uid='push_transactions')
