from kafka import KafkaConsumer

from chainchomp_adapter_kafka.messaging.IncomingMessageHandler import IncomingMessageHandler


class Subscriber:

    def __init__(self, kafka_consumer: KafkaConsumer, incoming_message_handler: IncomingMessageHandler):
        self.kafka_consumer = kafka_consumer
        self.incoming_message_handler = incoming_message_handler
        self.is_running = True

    def start_subscriber(self):
        while self.is_running:
            message = self.kafka_consumer.next()
            self.on_message(message)

    def stop_subscriber(self):
        self.is_running = False
        self.kafka_consumer.close()

    def on_message(self, data):
        self.incoming_message_handler.handle_incoming_message(data)
