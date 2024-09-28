from rest_framework import serializers
from core.models import User, FinancialInstrument, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FinancialInstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialInstrument
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

