from django.urls import path
from .views import CreateClient, GetUpdateClient, ListCreateMetric, ListCreateTransaction, ListCreateTask


urlpatterns = [
    path('client/', CreateClient.as_view(), name='create-client'),
    path('client/<username>/', GetUpdateClient.as_view(), name='get-update-client'),
    path('client/<username>/metric/', ListCreateMetric.as_view(), name='list-create-metric'),
    path('client/<username>/task/', ListCreateTask.as_view(), name='list-create-task'),
    path('client/<username>/transaction/', ListCreateTransaction.as_view(), name='list-create-transaction'),
]
