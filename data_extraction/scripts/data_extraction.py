import yfinance as yf
from django.utils import timezone
from ..models import StockData


def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    history = stock.history(period='1d')

    if not history.empty:
        last_row = history.iloc[-1]
        StockData.objects.create(
            symbol=symbol,
            open_price=last_row['Open'],
            high_price=last_row['High'],
            low_price=last_row['Low'],
            close_price=last_row['Close'],
            volume=last_row['Volume'],
            date=timezone.now(),
        )
