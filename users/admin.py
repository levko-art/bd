from django.contrib import admin

from .models import Account, Client, Counter, Transaction

admin.site.register(Account)
admin.site.register(Client)
admin.site.register(Counter)
admin.site.register(Transaction)
