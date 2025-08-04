import os
import json

FILE = "expenses_data.json"

def initialize():
    if os.path.exists(FILE):
        try:
            with open(FILE, 'r') as f:
                return json.load(f)
        except:
            print("Error reading expenses file. Creating new data.")
    
    return {
        "categories": ["home", "water", "elec", "internet"],
        "expenses": []
    }

def save(data):
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=2)