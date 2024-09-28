from celery import shared_task
from .data_extraction import fetch_stock_data


@shared_task
def update_stock_data():
    symbols = ['AAPL', 'GOOGL', 'MSFT']
    for symbol in symbols:
        fetch_stock_data(symbol)
