# utils/worker.py
from datetime import datetime
import asyncio
import logging

# Initialize logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Define Worker class
class Worker:
    def __init__(self, team, routine):
        self.team = team 
        self.routine = routine
        self.status = "Idle"
        self.last_active_time = datetime.now()

    async def handle_event(self, event):
        self.status = "Working"
        # Simulate event handling time based on routine and priority
        await asyncio.sleep(3) # 3 secs to handle event
        self.status = "Idle"
        self.last_active_time = datetime.now()
        logger.info(f"Event {event.event_id} handled by {self.team}")

        # work_time = PRIORITY_TIMEFRAMES[event.priority]
        # start_time = datetime.now()
        
    async def simulate_routine(self):
        while True:
            if self.routine == "Standard":
                await asyncio.sleep(20)
                self.status = "Idle"
                await asyncio.sleep(5)
            elif self.routine == "Intermittent":
                await asyncio.sleep(5) # Simulate short working time
                self.status = "Idle"
                await asyncio.sleep(5) # Idle time
            elif self.routine == "Concentrated":
                await asyncio.sleep(60)
                self.status = "Idle"
                await asyncio.sleep(60)
            self.status = "Working"

# Define Team class
class Team:
    def __init__(self, name, routine):
        self.name = name
        self.routine = routine
        self.workers = [Worker(name, routine) for _ in range(5)] # Assuming 5 workers / team

    async def assign_event(self, event):
        for worker in self.workers:
            if worker.status == "Idle":
                await worker.handle_event(event)
                return True
        return False