from rest_framework import serializers
from users.models import Client, Transaction, Counter


class ClientSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(max_length=40)
    personal_number = serializers.CharField(max_length=9)
    phone = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    viber = serializers.BooleanField(default=False)
    telegram = serializers.BooleanField(default=False)
    reserve_phone = serializers.CharField(max_length=10)
    housing_complex = serializers.CharField(max_length=15)
    region = serializers.CharField(max_length=10)
    district = serializers.CharField(max_length=20)
    town = serializers.CharField(max_length=25)
    street = serializers.CharField(max_length=20)
    building = serializers.IntegerField()
    house_building = serializers.IntegerField()
    flat = serializers.IntegerField()
    communal_service = serializers.BooleanField(default=False)
    communal_service_balance = serializers.DecimalField(max_digits=7, decimal_places=2, default=0)
    water = serializers.BooleanField(default=False)
    water_balance = serializers.BooleanField(default=0)
    water_counter = serializers.IntegerField(default=0)
    electricity = serializers.BooleanField(default=False)
    electricity_balance = serializers.BooleanField(default=0)
    electricity_counter = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.name = validated_data.get('name', instance.name)
        instance.personal_number = validated_data.get('personal_number', instance.personal_number)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.viber = validated_data.get('viber', instance.viber)
        instance.telegram = validated_data.get('telegram', instance.telegram)
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
        instance.communal_service_balance = validated_data.get('communal_service_balance', instance.communal_service_balance)
        instance.water = validated_data.get('water', instance.water)
        instance.water_balance = validated_data.get('water_balance', instance.water_balance)
        instance.water_counter = validated_data.get('water_counter', instance.water_counter)
        instance.electricity = validated_data.get('electricity', instance.electricity)
        instance.electricity_balance = validated_data.get('electricity_balance', instance.electricity_balance)
        instance.electricity_counter = validated_data.get('electricity_counter', instance.electricity_counter)


class TransactionSerializer(serializers.Serializer):
    transaction_date = serializers.DateField()
    transaction_time = serializers.TimeField()
    transaction_client = serializers.PrimaryKeyRelatedField(read_only=True)
    transaction_type = serializers.BooleanField(default=False)
    transaction_sum = serializers.DecimalField(max_digits=7, decimal_places=2, default=0)

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.transaction_date = validated_data.get('transaction_date', instance.transaction_date)
        instance.transaction_time = validated_data.get('transaction_time', instance.transaction_time)
        instance.transaction_client = validated_data.get('transaction_client', instance.transaction_client)
        instance.transaction_type = validated_data.get('transaction_type', instance.transaction_type)
        instance.transaction_sum = validated_data.get('transaction_sum', instance.transaction_sum)


class CounterSerializer(serializers.Serializer):

    types = ((0, 'Водопостачання'), (1, 'Електроенергія'))

    client = serializers.PrimaryKeyRelatedField(read_only=True)
    datetime = serializers.DateTimeField()
    counter_type = serializers.ChoiceField(choices=types)
    counter_value = serializers.IntegerField()

    def create(self, validated_data):
        return Counter.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.client = validated_data.get('client', instance.client)
        instance.datetime = validated_data.get('datetime', instance.datetime)
        instance.counter_type = validated_data.get('counter_type', instance.counter_type)
        instance.counter_value = validated_data.get('counter_value', instance.counter_value)
