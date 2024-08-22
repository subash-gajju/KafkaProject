import json
from kafka import KafkaConsumer
from django.utils import timezone
from datetime import datetime
import os
import django
import six
import sys

if sys.version_info >= (3, 12, 5):
    sys.modules['kafka.vendor.six.moves'] = six.moves

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kafkaproject.settings")
django.setup()

from face_embed.models import FaceEmbed

def kafka_consumer():
    consumer = KafkaConsumer(
        'face.embed.data',
        bootstrap_servers='localhost:9092',
        group_id='face_embed_group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    for message in consumer:
        data = message.value
        # Save data to Django model
        FaceEmbed.objects.create(
            id=data.get('id'),
            age=data.get('age'),
            emotion=data.get('emotion'),
            gender=data.get('gender'),
            timestamp=timezone.make_aware(datetime.fromisoformat(data.get('timestamp')))
        )
        print(f"Data received and saved: {data}")

if __name__ == "__main__":
    kafka_consumer()
