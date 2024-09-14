# main.py

from consumer import start_app
from producer import run_simulation

if __name__=="__main__":
    start_app() # Start consumer app
    file_path = "producer/events_data1.txt" # Path to event data
    run_simulation(file_path)    # Run producer simulation