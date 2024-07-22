from .run import app, logger, producer
from aiokakfa import errors


@app.post("/send/{topic}")
async def produce(topic: str, message: str):
    try:
        await producer.send_and_wait(topic, message.encode('utf-8'))
        logger.info(f"Produced message: {message} to topic: {topic}")
        return {"message": "Message sent successfully"}
    except errors.KafkaConnectionError as e:
        logger.error(f"Kafka connection error: {e}")
        return {"message": "Failed to send message"}
