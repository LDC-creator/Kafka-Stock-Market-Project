from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSystem

consumer = KafkaConsumer(
    'demo_test',
    bootstrap_servers=['54.163.213.19:9092'],
    value_deserializer=lambda x: loads(x.decode('utf-8')))

# for message in consumer:
#     print(message.value)

s3 = S3FileSystem()

for count, i in enumerate(consumer):
    with s3.open("s3://stock-market-project-kafka-luke/stock_market_{}.json".format(count), 'w') as file:
        json.dump(i.value, file)
