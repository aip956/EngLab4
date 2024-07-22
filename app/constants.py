from aiokafka import AIOKafkaProducer
import asyncio
import logging
import os


KAFKA_BOOTSTRAP_SERVER = os.getenv("KAFKA_BOOTSTRAP_SERVER", "localhost:9092")

logger = logging.getLogger("uvicorn.error")

loop = asyncio.get_event_loop()

producer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVER)