import os
import json

FILE = "finance_data.json"

def initialize():
    if os.path.exists(FILE):
        try:
            with open(FILE, 'r') as f:
                return json.load(f)
        except:
            print("Error reading finance file. Creating new data.")
    
    return {"total": 0.0, "bank_card": 0.0, "cash": 0.0}

def save(data):
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=2)