import json

from kafka import KafkaProducer

from chainchomp_adapter_kafka.kafka.producer.Publisher import Publisher


class Producer:

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda m: json.dumps(m).encode('utf-8')
        )
        self.publishers = {}

    def create_new_publisher(self, name) -> Publisher:
        publisher = Publisher(self.producer, name)
        self.publishers[name] = publisher
        return publisher
