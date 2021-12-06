from rest_framework import serializers
from users.models import Client, Transaction, Counter


__all__ = 'ClientSerializer', 'CounterSerializer'


class CounterSerializer(serializers.Serializer):

    types = ((0, 'Водопостачання'), (1, 'Електроенергія'))

    datetime = serializers.DateTimeField()
    type = serializers.ChoiceField(choices=types)
    value = serializers.CharField(max_length=10)

    def create(self, validated_data):
        return Counter.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.datetime = validated_data.get('datetime', instance.datetime)
        instance.value = validated_data.get('value', instance.value)


class ClientSerializer(serializers.Serializer):

    client_id = serializers.CharField(max_length=9)
    password = serializers.CharField(max_length=128)

    phone = serializers.CharField(max_length=10)

    housing_complex = serializers.CharField(max_length=15)
    region = serializers.CharField(max_length=10)
    district = serializers.CharField(max_length=20)
    town = serializers.CharField(max_length=30)
    street = serializers.CharField(max_length=20)
    building = serializers.IntegerField()
    house_building = serializers.IntegerField()
    flat = serializers.IntegerField()

    communal_service = serializers.BooleanField(default=False)
    communal_service_balance = serializers.DecimalField(max_digits=7, decimal_places=2, default=0)

    water = serializers.BooleanField(default=False)
    water_balance = serializers.DecimalField(max_digits=7, decimal_places=2, default=0)

    electricity = serializers.BooleanField(default=False)
    electricity_balance = serializers.DecimalField(max_digits=7, decimal_places=2, default=0)

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.housing_complex = validated_data.get('housing_complex', instance.housing_complex)
        instance.region = validated_data.get('region', instance.region)
        instance.district = validated_data.get('district', instance.district)
        instance.town = validated_data.get('town', instance.town)
        instance.street = validated_data.get('street', instance.street)
        instance.building = validated_data.get('building', instance.building)
        instance.house_building = validated_data.get('house_building', instance.house_building)
        instance.flat = validated_data.get('flat', instance.flat)
        instance.communal_service = validated_data.get('communal_service', instance.communal_service)
        instance.communal_service_balance = validated_data.get('communal_service_balance', instance.communal_service_balance)
        instance.water = validated_data.get('water', instance.water)
        instance.water_balance = validated_data.get('water_balance', instance.water_balance)
        instance.electricity = validated_data.get('electricity', instance.electricity)
        instance.electricity_balance = validated_data.get('electricity_balance', instance.electricity_balance)
        return instance

    def __str__(self):
        return 'Serializer for client model'


class TransactionSerializer(serializers.Serializer):
    date = serializers.DateField()
    time = serializers.TimeField()
    client = serializers.PrimaryKeyRelatedField(read_only=True)
    type = serializers.BooleanField(default=False)
    sum = serializers.DecimalField(max_digits=7, decimal_places=2, default=0)

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        raise NotImplementedError('`update()` must be implemented.')

    def __str__(self):
        return 'Serializer for transaction model'


# class CounterSerializer(serializers.Serializer):
#
#     types = ((0, 'Водопостачання'), (1, 'Електроенергія'))
#
#     client = serializers.PrimaryKeyRelatedField(read_only=True)
#     datetime = serializers.DateTimeField()
#     counter_type = serializers.ChoiceField(choices=types)
#     counter_value = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Counter.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.client = validated_data.get('client', instance.client)
#         instance.datetime = validated_data.get('datetime', instance.datetime)
#         instance.counter_type = validated_data.get('counter_type', instance.counter_type)
#         instance.counter_value = validated_data.get('counter_value', instance.counter_value)
