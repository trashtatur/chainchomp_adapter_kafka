from kafka import KafkaProducer

from chainchomp_adapter_kafka.kafka.Producer.Publisher import Publisher


class Producer:

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers='localhost:9092'
        )
        self.publishers = {}

    def create_new_publisher(self, name) -> Publisher:
        publisher = Publisher(self.producer, name)
        self.publishers[name] = publisher
        return publisher
