from django.urls import path
from .views import *


urlpatterns = [
    path('client/', CreateClient.as_view(), name='create-client'),
    path('client/<client_id>/', GetUpdateClient.as_view(), name='get-update-client'),
    path('client/<client_id>/counter/<counter_id>', GetUpdateCounter.as_view(), name='get-update-counter'),
    path('client/<client_id>/account/<account_id>', GetUpdateAccount.as_view(), name='get-update-account'),
    path('client/<client_id>/transaction/', ListCreateTransaction.as_view(), name='list-create-transaction'),
    path('client/<client_id>/transaction/<transaction_id>/', GetTransaction.as_view(), name='get-transaction'),
]
