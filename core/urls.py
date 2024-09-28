from django.urls import path
from .views import UserListCreateView, FinancialInstrumentListCreateView, TransactionListCreateView


urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user'),
    path('instruments/', FinancialInstrumentListCreateView.as_view(), name='instrument'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction'),
]
