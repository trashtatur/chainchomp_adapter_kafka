from chainchomp_adapter_kafka.socket.SocketEmitter import SocketEmitter


class IncomingMessageHandler:

    def __init__(self, socket_emitter: SocketEmitter):
        self.socket_emitter = socket_emitter

    def handle_incoming_message(self, data):
        pass