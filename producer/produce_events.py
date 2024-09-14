import asyncio
from aiokafka import AIOKafkaProducer
import json

KAFKA_BOOTSTRAP_SERVER = "localhost:9092"
TOPIC = "wedding_events"


# @app.post("/events")
# async def receive_event(event: Event):
#     valid_event_types = event_team_mapping.keys()
#     if event.event_type not in valid_event_types:
#         raise HTTPException(status_code=400, detail="Invalid event type")
#     # events.append(event)
#     logger.info(f"Received event: {event.event_id}")
#     # await dispatch_event(event)
#     await produce_event_to_kafka(event)
#     return{"status": "Event received"}

# async def produce_event_to_kafka(event):
#     try:
#         await producer.send_and_wait("events_topic", json.dumps(event.dict()).encode('utf-8'))
#         logger.info(f"Produced event: {event.event_id} to Kafka")
#     except errors.KafkaConnectionError as e:
#         logger.error(f"Kafka connection error: {e}")


async def produce_event(producer, event):
    event_data = json.dumps(event).encode("utf-8")
    await producer.send_and_wait(TOPIC, event_data)
    print(f"Produced event: {event['event_type']}")

async def run_simulation(file_path):
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVER)
    await producer.start()
    try:
        events = read_events_data(file_path)

        for event in events:
            await produce_event(producer, event)
            await asyncio.sleep(1) # simulate time between events
    finally:
        await producer.stop()

def read_events_data(file_path):
    with open(file_path, mode='r') as file:
        lines = file.readlines()

    events = []
    i = 0
    while i < len(lines):
        # Skip line if only a digit
        if lines[i].strip().isdigit():
            print("digit only")
            i += 1
            print(f"i: {i}")
            continue
        if i + 4 < len(lines):
            try:
                index_line = lines[i].strip()
                print(f"i, IndLine: {i}, {index_line}")
                event_type_line = lines[i + 1].strip()
                priority_line = lines[i + 2].strip()
                description_line = lines[i + 3].strip()
                timestamp_line = lines[i + 4].strip()

                if not (index_line.startswith("id\t") and 
                        event_type_line.startswith("event_type\t") and 
                        priority_line.startswith("priority\t") and 
                        description_line.startswith("description\t") and 
                        timestamp_line.startswith("timestamp\t")):
                    print(f"Unexpected format event data line {i}")
                    print(f"index_ln: {index_line}, event_ln: {event_type_line}, priority_ln: {priority_line}, desc_ln: {description_line}, time_ln: {timestamp_line}")
                    i += 5
                    continue

                index = index_line.split('\t')[1].strip('"\n ')
                event_type = event_type_line.split('\t')[1].strip('"\n ')
                priority = priority_line.split('\t')[1].strip('"\n ')
                description = description_line.split('\t')[1].strip('"\n ')
                timestamp = timestamp_line.split('\t')[1].strip('"\n ')

                if not (index and event_type and priority and description and timestamp):
                    print(f"Missing field in event at line {i}")
                    print(f"index: {index}, event: {event_type}, priority: {priority}, desc: {description}, time: {timestamp}")
                else:
                    events.append({
                        'event_id': index,
                        'event_type': event_type,
                        'priority': priority,
                        'description': description,
                        'timestamp': timestamp
                    })
                i += 6
            except IndexError as e:
                print(f"Error parsing at line {i}: {e}")
                break
        else:
            print(f"Incomplete event datastarting at line {i}")
            break
    return events

if __name__=="__main__":
    file_path = "producer/events_data1.txt" # Path to event data
    run_simulation(file_path)    # Run producer simulation
