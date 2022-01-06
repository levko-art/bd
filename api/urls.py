from django.urls import path
from .views import *


urlpatterns = [
    path('client/', CreateClient.as_view(), name='create-client'),
    path('client/<username>/', GetUpdateClient.as_view(), name='get-update-client'),
    path('client/<username>/transaction/', ListCreateTransaction.as_view(), name="list-create-transaction"),
]
