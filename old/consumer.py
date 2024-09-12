from .constants import *
from aiokafka import AIOKafkaConsumer
from ..old.run import loop, logger, consumed_messages, filtered_messages

consumed_messages = []
security_messages = []
clean_up_messages = []
catering_messages = []
officiant_messages = []
waiters_messages = []

# All the data topics
topics = ["person_fell", "broken_glass", "dirty_table", "brawl", "missing_rings", "missing_bride", "missing_groom", "feeling_ill", "injured_kid", "not_on_list", "bad_food", "music_too_loud", "music_too_low"]
SECURITY_TOPICS = ["brawl", "not_on_list", "person_fell", "injured_kid"]
CLEAN_UP_TOPICS = ["dirty_table", "broken_glass"]
CATERING_TOPICS = ["bad_food", "music_too_loud", "music_too_low", "feeling_ill"]
OFFICIANT_TOPICS = ["missing_rings", "missing_bride", "missing_groom"]
WAITERS_TOPICS = [ "broken_glass", "person_fell", "injured_kid", "feeling_ill"]


async def consume_all():
    consumer = AIOKafkaConsumer(
        *topics, # Unpack all topic names
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id= "AllConsumers")
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            consumed_messages.append({"topic": topic, "message": message})
            logger.info(f"Consumed_all message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()

async def consume_security():
    consumer = AIOKafkaConsumer(
        *SECURITY_TOPICS,
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id="Security")
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            security_messages.append({"topic": topic, "message": message})
            logger.info(f"Security message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()

async def consume_clean_up():
    consumer = AIOKafkaConsumer(
        *CLEAN_UP_TOPICS,
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id="Clean_Up")
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            clean_up_messages.append({"topic": topic, "message": message})
            logger.info(f"Clean_Up message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()


async def consume_catering():
    consumer = AIOKafkaConsumer(
        *CATERING_TOPICS, #Sub in KAFA_TOPIC later
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id="Catering")
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            catering_messages.append({"topic": topic, "message": message})
            logger.info(f"Catering message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()

async def consume_officiant():
    consumer = AIOKafkaConsumer(
        *OFFICIANT_TOPICS,
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id="Officiant")
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            officiant_messages.append({"topic": topic, "message": message})
            logger.info(f"Officiant message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()

async def consume_waiters():
    consumer = AIOKafkaConsumer(
        *WAITERS_TOPICS,
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id="Waiters")
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            waiters_messages.append({"topic": topic, "message": message})
            logger.info(f"Waiting message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()
