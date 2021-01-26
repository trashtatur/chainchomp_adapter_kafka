import asyncio

from chainchomp_adapter_kafka.socket.SocketClient import connect

loop = asyncio.get_event_loop()
loop.create_task(connect())
loop.run_forever()
