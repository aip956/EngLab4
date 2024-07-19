import requests

# FastAPI endpoint
url = "http://localhost:8008/tasks/"

# List of tasks
tasks = [
    {"title": "Task 1", "description": "Description for task 1"},
    {"title": "Task 2", "description": "Description for task 2"},
    {"title": "Task 3", "description": "Description for task 3"},
    {"title": "Task 4", "description": "Description for task 4"},
    {"title": "Task 5", "description": "Description for task 5"},
    {"title": "Task 6", "description": "Description for task 6"},
    {"title": "Task 7", "description": "Description for task 7"},
    {"title": "Task 8", "description": "Description for task 8"},
    {"title": "Task 9", "description": "Description for task 9"},
    {"title": "Task 10", "description": "Description for task 10"},
    {"title": "Task 11", "description": "Description for task 11"},
    {"title": "Task 12", "description": "Description for task 12"},
    {"title": "Task 13", "description": "Description for task 13"},
    {"title": "Task 14", "description": "Description for task 14"},
    {"title": "Task 15", "description": "Description for task 15"},
    {"title": "Task 16", "description": "Description for task 16"},
    {"title": "Task 17", "description": "Description for task 17"},
    {"title": "Task 18", "description": "Description for task 18"},
    {"title": "Task 19", "description": "Description for task 19"},
    {"title": "Task 20", "description": "Description for task 20"},
    {"title": "Task 21", "description": "Description for task 21"},
    {"title": "Task 22", "description": "Description for task 22"},
    {"title": "Task 23", "description": "Description for task 23"},
    {"title": "Task 24", "description": "Description for task 24"},
    {"title": "Task 25", "description": "Description for task 25"},
    {"title": "Task 26", "description": "Description for task 26"},
    {"title": "Task 27", "description": "Description for task 27"},
    {"title": "Task 28", "description": "Description for task 28"},
    {"title": "Task 29", "description": "Description for task 29"},
    {"title": "Task 30", "description": "Description for task 30"},
    {"title": "Task 31", "description": "Description for task 31"},
    {"title": "Task 32", "description": "Description for task 32"},
    {"title": "Task 33", "description": "Description for task 33"},
    {"title": "Task 34", "description": "Description for task 34"},
    {"title": "Task 35", "description": "Description for task 35"},
    {"title": "Task 36", "description": "Description for task 36"},
    {"title": "Task 37", "description": "Description for task 37"},
    {"title": "Task 38", "description": "Description for task 38"},
    {"title": "Task 39", "description": "Description for task 39"},
    {"title": "Task 40", "description": "Description for task 40"},
    {"title": "Task 41", "description": "Description for task 41"},
    {"title": "Task 42", "description": "Description for task 42"},
    {"title": "Task 43", "description": "Description for task 43"},
    {"title": "Task 44", "description": "Description for task 44"},
    {"title": "Task 45", "description": "Description for task 45"},
    {"title": "Task 46", "description": "Description for task 46"},
    {"title": "Task 47", "description": "Description for task 47"},
    {"title": "Task 48", "description": "Description for task 48"},
    {"title": "Task 49", "description": "Description for task 49"},
    {"title": "Task 50", "description": "Description for task 50"}
]

# Send tasks to FastAPI
for task in tasks:
    response = requests.post(url, json=task)
    if response.status_code != 200:
        print(f"Failed to create task: {task['title']}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
    else:
        try: 
            response_data = response.json()
        except requests.exceptions.JSONDecodeError:
            response_data = response.text
        print(response.json())