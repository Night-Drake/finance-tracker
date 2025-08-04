import os
import json

FILE = "finance_settings.json"
DEFAULT = {
    "warning_thresholds": {
        "food": 300, "shopping": 200, "entertainment": 150,
        "transport": 100, "other": 500
    },
    "monthly_income": 400
}

def initialize():
    if os.path.exists(FILE):
        try:
            with open(FILE, 'r') as f:
                return json.load(f)
        except:
            print("Error reading settings. Using defaults.")
    return DEFAULT

def save(data):
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=2)