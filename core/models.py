from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # password = models.PasswordField(max_length=100)
    join_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FinancialInstrument(models.Model):
    instrument_id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    instrument_type = models.CharField(max_length=50)
    current_price = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.symbol})"


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]

    transaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instrument = models.ForeignKey(FinancialInstrument, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.transaction_type.capitalize()} {self.amount} {self.instrument.currency} of {self.instrument.symbol}"
