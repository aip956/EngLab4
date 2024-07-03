# Welcome to Eng Lab 4, Event-Driven Microservice


## Task

## Description


## Pieces

### Flow
#### Task Assignment
    Coordinator (Producer) sends event
    Coordinator publishes to the Organizer (Broker)
    Worker Teams (Consumers) subscribe to event
    Worker receives event
    Worker service updates the database and acknowledges event

#### Notification
    Coordinator generates a "Notification" event
    Producer service publishes event to the Broker
    Notification service subscribes to "Notification" events
    Notification service receives the event and sends a notification
    Notification service updates the database and acknowledges the event

####

## Prerequisites

**Docker**:

- Docker Engine: For installation instructions, refer to the Docker documentation: https://docs.docker.com/engine/install/

## Installation

1. **Build the Docker Image & Run the API**:
   ```bash
   docker-compose up -d
    ```
2. **Run Testing suite**:
   ```bash
   docker-compose run test  
   ```
The testing report is logged in pytest_logs.txt, located in the main directory.   
Access FastAPI Swagger:
http://127.0.0.1:8000/docs
http://localhost:8000/docs


## Usage
Post a message:
topic: my_topic
message: Hello Kafka!
Should return code 200