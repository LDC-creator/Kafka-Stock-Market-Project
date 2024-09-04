
import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['54.163.213.19:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

# Send a test message
producer.send('demo_test', value={"message": "Hello World"})
producer.flush()  # Ensure the message is sent before continuing

# Load data from CSV file
df = pd.read_csv("/Users/User/Kafka-stock-market-project/indexProcessed.csv")

# Continuously send messages from the CSV data
while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]  # Pick a random record from the DataFrame
    producer.send('demo_test', value=dict_stock)  # Send the data to Kafka
    print(f"Sent message: {dict_stock}")  # Print the message to confirm it was sent
    sleep(1)  # Sleep for 1 second

# Flush any remaining messages
producer.flush()  # Clear any unsent messages from the buffer
