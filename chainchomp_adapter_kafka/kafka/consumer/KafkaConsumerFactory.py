from kafka import KafkaConsumer


def create(address, topic) -> KafkaConsumer:
    return KafkaConsumer(
        topic,
        group_id=topic,
        bootstrap_servers=address,
        auto_offset_reset='earliest',
    )
