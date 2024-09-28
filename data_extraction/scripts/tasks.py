from celery import shared_task
from .data_extraction import fetch_stock_data
from kafka import KafkaProducer
import json


@shared_task
def update_stock_data():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    symbols = ['AAPL', 'GOOGL', 'MSFT']
    for symbol in symbols:
        try:
            data = fetch_stock_data(symbol)
            send_stock_data(producer, symbol, data)
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")


def send_stock_data(producer, symbol, data):
    try:
        producer.send('stock_topic', {'symbol': symbol, 'data': data})
        producer.flush()
    except Exception as e:
        print(f"Error sending data to Kafka: {e}")
