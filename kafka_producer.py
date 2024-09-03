
from kafka import KafkaProducer
from json import dumps

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['54.163.213.19:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

# Send a message
producer.send('demo_test', value={"message": "Hello World"})
producer.flush()  # Ensure data is sent before terminating


