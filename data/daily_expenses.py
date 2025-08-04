import os
import json

FILE = "daily_expenses.json"

def initialize():
    if os.path.exists(FILE):
        try:
            with open(FILE, 'r') as f:
                return json.load(f)
        except:
            print("Error reading daily expenses file. Creating new data.")
    
    return {"expenses": []}

def save(data):
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=2)