from datetime import datetime

def get_valid_date(prompt):
    """Get a valid date from user with today as default"""
    while True:
        
        date_str = input(prompt).strip()
        if not date_str:
            return datetime.now().strftime("%Y-%m-%d")
        
        try:
 
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")

