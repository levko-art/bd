from django.urls import path
from .views import *


urlpatterns = [
    path('client/', CreateClient.as_view(), name='create-client'),
    path('client/<client_id>/', GetClient.as_view(), name='get_client'),

    path('client/<int:client_id>/transaction', ListCreateTransaction.as_view(), name="list-create-transaction"),
    path('client/<int:client_id>/transaction/<int:transaction_id>', GetTransaction.as_view(), name="transaction-by-id"),
    # path('client/<int:client_id>/counter', ListCreateCounter.as_view(), name="list-create-counter")
]
