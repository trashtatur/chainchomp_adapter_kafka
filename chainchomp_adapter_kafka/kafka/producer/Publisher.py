from chainchomplib.adapterlayer.Message import Message
from kafka import KafkaProducer


class Publisher:
    def __init__(self, kafka_producer: KafkaProducer, name: str):
        self.kafka_producer = kafka_producer
        self.name = name

    def publish(self, message: Message):
        self.kafka_producer.send(self.name, message.get_serialized())
