from rest_framework import generics
from users.models import Client, Transaction, Counter
from users.serializers import ClientSerializer, TransactionSerializer, CounterSerializer


class ListCreateTransactions(generics.ListCreateAPIView):

    """
    client/<int:client_id>/transaction
    """

    queryset = Transaction.objects
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return super().get_queryset().filter(transaction_client__user=self.request.user)

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class GetTransactionById(generics.ListAPIView):

    """
    client/<int:client_id>/transaction/<int:transaction_id>
    """

    queryset = Transaction.objects
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs['transaction_id'])


class CreateClient(generics.CreateAPIView):

    """
    client/
    """

    queryset = Client.objects
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class GetClientById(generics.CreateAPIView):

    """
    client/<int:client_id>
    """

    queryset = Client.objects
    serializer_class = ClientSerializer

    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs['client_id'])


class ListCreateCounter(generics.ListCreateAPIView):

    """
    client/<int:client_id>/counter
    """

    queryset = Counter.objects
    serializer_class = CounterSerializer

    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs['counter_id'])

    def perform_create(self, serializer):
        return super().perform_create(serializer)
