from django.shortcuts import render

from rest_framework import generics
from .models import User, FinancialInstrument, Transaction
from .serializers import UserSerializer, FinancialInstrumentSerializer, TransactionSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FinancialInstrumentListCreateView(generics.ListCreateAPIView):
    queryset = FinancialInstrument.objects.all()
    serializer_class = FinancialInstrumentSerializer


class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
