from pydantic import BaseModel

from .worker import Team

# Define Event class
class Event(BaseModel):
    event_id: int
    event_type: str
    priority: str
    description: str
    timestamp: str


# Timeframes for priorities in secs
PRIORITY_TIMEFRAMES = {
    "High": 5,
    "Medium": 10,
    "Low": 15
}

# New topics for v2 of assignment
topics = ["accident", "bad_food", "brawl", "broken_glass", "broken_itens", "bride", "dirty_floor", "dirty_table", "feeling_ill", "groom", "injured_kid", "missing_bride", "missing_groom", "missing_rings", "music_too_loud", "music_too_low", "music", "not_on_list", "person_fell"]


SECURITY_TOPICS = ["brawl", "not_on_list", "accident", "person_fell", "injured_kid"]
CLEAN_UP_TOPICS = ["dirty_table", "broken_glass", "broken_itens", "dirty_floor"]
CATERING_TOPICS = ["bad_food", "music", "music_too_loud", "music_too_low", "feeling_ill"]
OFFICIANT_TOPICS = ["missing_rings", "missing_bride", "missing_groom", "bride", "groom"]
WAITERS_TOPICS = [ "broken_glass", "person_fell", "injured_kid", "feeling_ill", "broken_itens", "accident", "bad_food"]

    
# Initialize teams
teams = {
    "Security": Team("Security", "Standard"),
    "Clean_Up": Team("Clean_Up", "Intermittent"),
    "Catering": Team("Catering", "Concentrated"), 
    "Officiant": Team("Officiant", "Concentrated"),
    "Waiters": Team("Waiters", "Standard")
}

# Event type to team mapping
event_team_mapping = {
        "accident": ["Security", "Waiters"],
        "bad_food": ["Catering", "Waiters"], 
        "brawl": ["Secruity"],
        "broken_glass": ["Clean_Up", "Waiters"], 
        "broken_itens": ["Clean_Up", "Waiters"], 
        "bride": ["Officiant"], 
        "dirty_floor": ["Clean_Up"], 
        "dirty_table": ["Clean_Up"], 
        "feeling_ill": ["Catering"], 
        "groom": ["Officiant"], 
        "injured_kid": ["Security", "Waiters"], 
        "missing_bride": ["Officiant"], 
        "missing_groom": ["Officiant"], 
        "missing_rings": ["Officiant"], 
        "music_too_loud": ["Catering"], 
        "music_too_low": ["Catering"], 
        "music": ["Catering"], 
        "not_on_list": ["Security"], 
        "person_fell": ["Security", "Waiters"]
    }

# For getting events by team
# consumed_messages = []
security_messages = []
clean_up_messages = []
catering_messages = []
officiant_messages = []
waiters_messages = []

