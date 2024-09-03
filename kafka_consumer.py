from kafka import KafkaConsumer
from json import loads,dumps
import json
from time import sleep

consumer = KafkaConsumer(
    'demo_test',
    bootstrap_servers=['54.163.213.19:9092'],
    value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    print(f"Consumed message: {message.value}")

