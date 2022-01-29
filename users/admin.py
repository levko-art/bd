from django.contrib import admin

from .models import Account, Client, Counter, Metric, Task, Transaction

admin.site.register(Account)
admin.site.register(Client)
admin.site.register(Counter)
admin.site.register(Metric)
admin.site.register(Task)
admin.site.register(Transaction)
