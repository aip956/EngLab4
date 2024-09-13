# event.py
from pydantic import BaseModel

# Define Event class
class Event(BaseModel):
    event_id: int
    event_type: str
    priority: str
    description: str
    timestamp: str