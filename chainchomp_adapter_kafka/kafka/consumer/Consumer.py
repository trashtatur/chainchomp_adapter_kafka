from chainchomp_adapter_kafka.kafka.consumer import KafkaConsumerFactory
from chainchomp_adapter_kafka.kafka.consumer.Subscriber import Subscriber
from chainchomp_adapter_kafka.messaging.IncomingMessageHandler import IncomingMessageHandler
from chainchomp_adapter_kafka.socket.SocketEmitter import SocketEmitter


class Consumer:

    def __init__(self, socket_emitter: SocketEmitter):
        self.subscribers = {}
        self.socket_emitter = socket_emitter

    def create_new_subscriber(self, remote_address: str, name: str):
        kafka_consumer = KafkaConsumerFactory.create(remote_address, name)
        subscriber = Subscriber(kafka_consumer, IncomingMessageHandler(self.socket_emitter))
        self.subscribers[name] = subscriber
        return subscriber
