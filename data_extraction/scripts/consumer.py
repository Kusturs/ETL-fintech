from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'stock_topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    symbol = message.value['symbol']
    data = message.value['data']
    print(f"Received stock data for {symbol}: {data}")
