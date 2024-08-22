import random
from kafka import KafkaProducer
import json
from datetime import datetime
import time
import six
import sys

if sys.version_info >= (3, 12):
    sys.modules['kafka.vendor.six.moves'] = six.moves

def generate_random_data():
    return {
        "id": random.randint(1, 1000),
        "age": random.randint(18, 70),
        "emotion": random.choice(["happy", "sad", "angry", "neutral"]),
        "gender": random.choice(["male", "female", "other"]),
        "timestamp": datetime.now().isoformat()
    }

def kafka_producer():
    producer = KafkaProducer(bootstrap_servers='localhost:9092', 
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    while True:
        data = generate_random_data()
        producer.send('face.embed.data', value=data)
        print(f"Data sent: {data}")
        time.sleep(2)  # Adjust the interval as needed

if __name__ == "__main__":
    kafka_producer()
