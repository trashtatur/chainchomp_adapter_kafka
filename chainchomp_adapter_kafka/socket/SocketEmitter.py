import asyncio

from chainchomplib.data import SocketEvents
from socketio import AsyncClient


class SocketEmitter:

    def __init__(self, socket_client: AsyncClient):
        self.socket_client = socket_client

    def emit_to_chainchomp_core(self, data):
        asyncio.run(self.socket_client.emit(
            SocketEvents.RECEIVE_MESSAGE_FROM_ADAPTER,
            data
        ))
