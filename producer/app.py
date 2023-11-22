from json import dumps
from flask import Flask, request
from kafka import KafkaProducer, KafkaConsumer
import pymongo

app = Flask(__name__)

try:
    client = pymongo.MongoClient("mongodb+srv://souvik_chatterjee:Jarvis9933@cluster0.lqkug31.mongodb.net/?retryWrites=true&w=majority")
    client.server_info()
    db = client.shipping
    print(" * DB connection established...")

except pymongo.errors.ServerSelectionTimeoutError as err:
    print(" * Failed to connect DB", err)



@app.route("/")
def hello_world():
    return "<p>Hello, World! from producer</p>"

@app.route("/create", methods=["POST"])
def create():
    
    try:
        shipping_data = request.json

        topic_name = "shipping_data"

        producer = KafkaProducer(
            bootstrap_servers=["kafka:9093"],
            value_serializer=lambda x: dumps(x, default=str).encode("utf-8"),
        )
        
        producer.send(topic_name, value=shipping_data)
        
        producer.flush()
        
        collection = db.producer
        collection.insert_one(shipping_data)
        
        data = shipping_data
        
    except Exception as e:
        data = {"error": e} 
    
    response_data = {
        "message": "Shipping data has been created successfully.",
        "success": True,
        "result": {"data": data},
    }
    return dumps(response_data, default=str)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)