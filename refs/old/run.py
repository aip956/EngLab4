from fastapi import FastAPI
from contextlib import asynccontextmanager
from aiokafka import errors 
import asyncio

from .constants import *
from .consumer import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    print("Application startup")
    try:
        await producer.start()
        logger.info("Kafka producer started")
        asyncio.create_task(consume_all())
        asyncio.create_task(consume_security())
        asyncio.create_task(consume_clean_up())
        asyncio.create_task(consume_catering())
        asyncio.create_task(consume_officiant())
        asyncio.create_task(consume_waiters())
        logger.info("Kafka consumer tasks created")
    except errors.KafkaConnectionError as e:
        logger.error(f"Kafka connection error: {e}")
    yield
    # Shutdown code
    print("Application shutdown")
    await producer.stop()
    logger.info("Kafka producer stopped")

app = FastAPI(lifespan=lifespan)


@app.get("/messages")
def get_messages():
    logger.info(f"Returning consumed messages: {consumed_messages}")
    return {"All messages": consumed_messages}

@app.get("/security_messages")
def get_security_messages():
    logger.info(f"Returning security messages: {security_messages}")
    return {"security messages": security_messages}

@app.get("/clean_up_messages")
def get_clean_up_messages():
    logger.info(f"Returning clean_up messages: {clean_up_messages}")
    return {"clean_up messages": clean_up_messages}

@app.get("/catering_messages")
def get_catering_messages():
    logger.info(f"Returning catering messages: {catering_messages}")
    return {"catering messages": catering_messages}

@app.get("/officiant_messages")
def get_officiant_messages():
    logger.info(f"Returning officiant messages: {officiant_messages}")
    return {"officiant messages": officiant_messages}

@app.get("/waiters_messages")
def get_waiters_messages():
    logger.info(f"Returning waiter messages: {waiters_messages}")
    return {"waiters messages": waiters_messages}