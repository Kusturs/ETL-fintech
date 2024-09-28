from django.db import models


class StockData(models.Model):
    symbol = models.CharField(max_length=10)
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    volume = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.symbol} - {self.date}"
