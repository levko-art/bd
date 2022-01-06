from rest_framework import serializers
from users.models import Client, Transaction, Counter


__all__ = 'ClientSerializer', 'CounterSerializer', 'TransactionSerializer'


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
        instance.save()
        return instance


class ClientSerializer(serializers.Serializer):

    client_full_name = serializers.CharField(max_length=60)

    username = serializers.CharField(max_length=9)
    password = serializers.CharField(max_length=128)

    phone = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=30)
    reserve_phone = serializers.CharField(max_length=10)

    housing_complex = serializers.CharField(max_length=15)
    region = serializers.CharField(max_length=10)
    district = serializers.CharField(max_length=20)
    town = serializers.CharField(max_length=30)
    street = serializers.CharField(max_length=20)
    building = serializers.IntegerField()
    house_building = serializers.IntegerField()
    flat = serializers.IntegerField()

    communal_service = serializers.BooleanField(default=False)
    water = serializers.BooleanField(default=False)
    electricity = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.reserve_phone = validated_data.get('reserve_phone', instance.reserve_phone)
        instance.housing_complex = validated_data.get('housing_complex', instance.housing_complex)
        instance.region = validated_data.get('region', instance.region)
        instance.district = validated_data.get('district', instance.district)
        instance.town = validated_data.get('town', instance.town)
        instance.street = validated_data.get('street', instance.street)
        instance.building = validated_data.get('building', instance.building)
        instance.house_building = validated_data.get('house_building', instance.house_building)
        instance.flat = validated_data.get('flat', instance.flat)
        instance.communal_service = validated_data.get('communal_service', instance.communal_service)
        instance.water = validated_data.get('water', instance.water)
        instance.electricity = validated_data.get('electricity', instance.electricity)
        instance.save()
        return instance

    def __str__(self):
        return 'Serializer for client model'


class TransactionSerializer(serializers.Serializer):

    types = ((0, 'Нарахування'), (1, 'Оплата'))
    appointments = ((0, 'Комунальний сервіс'), (1, 'Водопостачання'), (2, 'Електропостачання'))

    date = serializers.DateField()
    time = serializers.TimeField()
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='username')
    type = serializers.ChoiceField(choices=types)
    amount = serializers.DecimalField(max_digits=7, decimal_places=2, default=0)
    appointment = serializers.ChoiceField(choices=types)

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        raise NotImplementedError('`update()` must be implemented.')

    def __str__(self):
        return 'Serializer for transaction model'
