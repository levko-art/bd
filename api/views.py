import django_filters
from rest_framework import generics

from api.filters import TaskFilter, TransactionFilter
from users.models import Client, Metric, Task, Transaction
from api.paginations import TaskPagination, TransactionPagination
from api.serializers import ClientSerializer, MetricSerializer, TaskSerializer, TransactionSerializer

__all__ = 'CreateClient', 'GetUpdateClient', 'ListCreateTransaction', 'ListCreateMetric', 'ListCreateTask'


class CreateClient(generics.CreateAPIView):

    """
    Create client
    [POST] api/client/
    """

    queryset = Client.objects
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class GetUpdateClient(generics.RetrieveUpdateAPIView):

    """
    Get & update client by username
    [GET|PUT] api/client/<username>/
    """

    queryset = Client.objects
    serializer_class = ClientSerializer
    lookup_field = 'username'

    def get_queryset(self):
        return super().get_queryset()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ListCreateTransaction(generics.ListCreateAPIView):

    """
    List & create transaction
    [GET|POST] api/client/<username>/transaction/
    """

    queryset = Transaction.objects
    serializer_class = TransactionSerializer
    lookup_field = 'username'
    pagination_class = TransactionPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = TransactionFilter

    def get_queryset(self):
        return super().get_queryset().filter(client=self.request.user)

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class ListCreateMetric(generics.ListCreateAPIView):
    """
    List & create task
    [GET|POST] api/client/<username>/task/
    """

    queryset = Metric.objects
    serializer_class = MetricSerializer
    lookup_field = 'username'

    def get_queryset(self):
        return super().get_queryset().filter(client=self.request.user)

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class ListCreateTask(generics.ListCreateAPIView):
    """
    List & create task
    [GET|POST] api/client/<username>/task/
    """

    queryset = Task.objects
    serializer_class = TaskSerializer
    lookup_field = 'username'
    pagination_class = TaskPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = TaskFilter

    def get_queryset(self):
        return super().get_queryset().filter(client=self.request.user)

    def perform_create(self, serializer):
        return super().perform_create(serializer)
