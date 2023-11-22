# consumer.py

from json import loads
from flask import Flask
from kafka import KafkaConsumer
import pymongo

app = Flask(__name__)

try:
    client = pymongo.MongoClient("mongodb+srv://souvik_chatterjee:Jarvis9933@cluster0.lqkug31.mongodb.net/?retryWrites=true&w=majority")
    client.server_info()
    db = client.shipping
    print(" * DB connection established...")

except pymongo.errors.ServerSelectionTimeoutError as err:
    print(" * Failed to connect DB", err)


collection = db.consumer


topic_name = "shipping_data"


consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers='kafka:9093',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)


for message in consumer:
    ship_data = message.value
    collection.insert_one(ship_data)


consumer.close()

