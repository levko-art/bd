from rest_framework import generics, permissions
from users.models import Client, Transaction, Counter
from users.serializers import ClientSerializer, TransactionSerializer, CounterSerializer


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
    Get & update client by UUID
    [GET|PUT] api/client/<client_id>/
    """

    queryset = Client.objects
    serializer_class = ClientSerializer
    lookup_url_kwarg = 'client_id'

    def get_queryset(self):
        return super().get_queryset()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class GetUpdateCounter(generics.RetrieveUpdateAPIView):

    """
    Get & update counter by UUID
    [GET|PUT] api/client/<client_id>/
    """

    queryset = Counter.objects
    serializer_class = CounterSerializer
    lookup_url_kwarg = 'client_id'

    def get_queryset(self):
        return super().get_queryset()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ListCreateTransaction(generics.ListCreateAPIView):

    """
    Create & get list of transactions
    [POST|GET] api/client/<client_id>/transaction/
    """

    queryset = Transaction.objects
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def get_queryset(self):
        return super().get_queryset().filter(client__id=self.kwargs['client'])


class GetTransaction(generics.CreateAPIView):

    """
    Get transaction by UUID
    [GET] api/client/<client_id>/transaction/<transaction_id>/
    """

    queryset = Transaction.objects
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs['client_id'])

# class ListCreateCounter(generics.ListCreateAPIView):
#
#     """
#     client/<int:client_id>/counter
#     """
#
#     queryset = Counter.objects
#     serializer_class = CounterSerializer
#
#     def get_queryset(self):
#         return super().get_queryset().filter(id=self.kwargs['counter_id'])
#
#     def perform_create(self, serializer):
#         return super().perform_create(serializer)
