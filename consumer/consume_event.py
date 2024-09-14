from fastapi import FastAPI, errors
from supabase import create_client
from aiokafka import  AIOKafkaConsumer, errors
from pydantic import ValidationError

import logging
import os
import asyncio
from datetime import datetime
import json

from utils import *
from .events import *

# Initialize API
app = FastAPI()

# Connect Database
supabase = create_client(url, key)

# Initialize logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Kafka Configuration
KAFKA_BOOTSTRAP_SERVER = os.getenv("KAFKA_BOOTSTRAP_SERVER", "localhost:9092")

stress_level = 0
events = []
loop = asyncio.get_event_loop()


@app.on_event("startup")
async def on_startup():
    app.state.consumer = AIOKafkaConsumer(
        'wedding_events',
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id="event_group"
    )

    try:
        asyncio.create_task(consume_events(app.state.consumer))
        logger.info("Kafka consumer task created")
    except errors.KafkaConnectionError as e:
        logger.error(f"Kafka connection error: {e}")


@app.on_event("shutdown")
async def on_shutdown():
    await app.state.consumer.stop() # Stop the Kafka consumer
    logger.info("Kafka producer stopped")

# For the teams' messages
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



# Marry Me Organizer to dispatch events
async def dispatch_event(event):
    global stress_level, security_messages, clean_up_messages, catering_messages, officiant_messages, waiters_messages
    try:
        event_type = event.event_type
        event_id = event.event_id
        teams = event_team_mapping.get(event_type)
        logger.info(f"194Event {event_id} of type {event_type} mapped to team {teams}")
        
        if teams:
            event_handled = False
            start_time = datetime.now()

            for team_name in teams:
                team = await get_team_for_event(team_name)
                logger.info(f"200Dispatched {event_type} event {event_id} with team {team_name}")
                
                if team:
                    logger.info(f"202Adding {event_type} event {event_id} by team {team_name}.")
                    # Store event in event type list
                    if team_name == "Security":
                        security_messages.append(event)
                        logger.info(f"Appended security_messages: {security_messages}")
                    elif team_name == "Clean_Up":
                        clean_up_messages.append(event)
                    elif team_name == "Catering":
                        catering_messages.append(event)
                        logger.info(f"Appended catering_messages: {catering_messages}")
                    elif team_name == "Officiant":
                        officiant_messages.append(event)
                        logger.info(f"Appended officiant_messages: {officiant_messages}")
                    elif team_name == "Waiters":
                        waiters_messages.append(event)
                        logger.info(f"Appended waiters_messages: {waiters_messages}")

                    if await team.assign_event(event):
                        event_handled = True
                        logger.info(f"Event {event_id} handled by team {team_name}")
                        # break
                    else:
                        logger.warning(f"Team {team_name} unable to handle event type {event_type} eventID {event_id}")
            if not event_handled:
                elapsed_time = (datetime.now() - start_time).seconds
                if elapsed_time > PRIORITY_TIMEFRAMES[event.priority]:
                    stress_level += 1
                    logger.warning(f"Dispatched {event_type} event {event_id} not handled by team {team_name}. Stress level increased to {stress_level}")
        else:
            stress_level += 1
            logger.warning(f"200Unknown team or event type: {event_type}. Stress level increased to {stress_level}")
    except Exception as e:
        stress_level += 1
        logger.warning (f"Event {event_id} could not be handled in time. Stress level increased to {stress_level}")
        logger.error(f"Error handling event {event_id}: {e}")

async def get_team_for_event(team_name):
    team = teams.get(team_name)
    if team:
        logger.info(f"240 team_name: {team_name}")
    else:
        logger.warning(f"242Team {team_name} not found")
    return team

# Kafka consumer function
async def consume_events(consumer):
    await consumer.start()
    try:
        async for msg in consumer:
            event_data = json.loads(msg.value.decode("utf-8"))
            if 'event_id' not in event_data or 'timestamp' not in event_data:
                logger.error(f"229Missing field: {event_data}")
                continue
            try:
                event = Event(**event_data)
                events.append(event)
                await dispatch_event(event)
                logger.info(f"230Consumed and processed event: {event.event_type}")
                # ADD event to db
            except ValidationError as e:
                logger.error(f"Validation error for event data: {event_data} - {e.errors()}")
            except Exception as e:
                logger.error(f"Validation error for event data: {event_data} - {e}")
    except errors.KafkaError as e:
        logger.error(f"Kafka error: {e}")
    finally:
        await consumer.stop()

async def handle_event(event):
    global stress_level
    try:
        event_type = event.get("event_type")
        event_id = event.get("event_id")
        if event_type == "wedding":
            team = await get_team_for_event(event_type)
            # Perform actions with the team
            logger.info(f"Handled wedding event {event_id} with team {team}")
        else:
            logger.warning(f"210 type: {event_type}")
    except Exception as e:
        stress_level += 1
        logger.warning(f"Event {event_id} could not be handled in tiem. Stress level increased to {stress_level}")
        logger.error(f"Error handling event {event_id}: {e}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)