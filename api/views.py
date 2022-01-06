import django_filters
from rest_framework import generics

from users.filters import TransactionFilter
from users.models import Client, Transaction
from users.paginations import TransactionPagination
from users.serializers import ClientSerializer, TransactionSerializer


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
    Create transaction
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
