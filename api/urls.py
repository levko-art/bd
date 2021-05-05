from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = {
    path('client/', CreateClient, name="create-client"),
    path('client/<int:client_id>', GetClientById, name="client-by-id"),
    path('client/<int:client_id>/transaction', ListCreateTransactions.as_view(), name="list-create-transaction"),
    path('client/<int:client_id>/transaction/<int:transaction_id>', GetTransactionById.as_view(), name="transaction-by-id"),
    path('client/<int:client_id>/counter', ListCreateCounter.as_view(), name="list-create-counter")
}

urlpatterns = format_suffix_patterns(urlpatterns)
