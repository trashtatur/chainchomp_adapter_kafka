from threading import Thread
from kafka import KafkaConsumer
from kafka.consumer.fetcher import ConsumerRecord

from chainchomp_adapter_kafka.messaging.IncomingMessageHandler import IncomingMessageHandler


class Subscriber(Thread):

    def __init__(self, kafka_consumer: KafkaConsumer, incoming_message_handler: IncomingMessageHandler):
        super().__init__()
        self.kafka_consumer = kafka_consumer
        self.incoming_message_handler = incoming_message_handler
        self.is_running = True

    def run(self) -> None:
        while self.is_running:
            print('started thread for subscriber')
            message: ConsumerRecord
            for message in self.kafka_consumer:
                self.on_message(message.value)

    def stop_subscriber(self):
        self.is_running = False
        self.kafka_consumer.close()

    def on_message(self, data):
        self.incoming_message_handler.handle_incoming_message(data)
