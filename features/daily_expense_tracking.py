from data import daily_expenses
from features.balance_management import update_balance
from utils import get_valid_date

def add_expense(daily_exps, finance_data):
    try:
        description = input("\nWhat did you spend on? ").strip().lower()
        if not description:
            print("Description cannot be empty!")
            return
            
        amount = float(input("Amount spent: $"))
        if amount <= 0:
            print("Amount must be positive!")
            return         

        if finance_data["cash"] < amount:
            print(f"Error: Not enough cash! Available: ${finance_data['cash']:.2f}")
            return
        
        date_str = get_valid_date("Date (YYYY-MM-DD, enter for today): ")
        
        if update_balance(finance_data, "cash", amount, "subtract"):
            daily_exps["expenses"].append({
                "description": description,
                "amount": amount,
                "date": date_str,
                "reviewed": False
            })
            print(f"Added daily expense: ${amount:.2f} for {description} on {date_str}")
            print(f"New cash balance: ${finance_data['cash']:.2f}")
        
    except ValueError as e:
        print(f"Invalid input: {e}")


def review_expenses(daily_exps):
    unreviewed = [e for e in daily_exps["expenses"] if not e["reviewed"]]
    
    if not unreviewed:
        print("\nAll expenses reviewed!")
        return
        
    print("\nUnreviewed Expenses:")
    print("---------------------")
    
    for i, expense in enumerate(unreviewed, 1):
        print(f"{i}. {expense['date']}: {expense['description']} - ${expense['amount']:.2f}")
    
    try:
        choice = input("\nEnter number to mark reviewed (or 'all'): ")
        if choice.lower() == 'all':
            for expense in unreviewed:
                expense["reviewed"] = True
            print("Marked all as reviewed!")
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(unreviewed):
                unreviewed[idx]["reviewed"] = True
                print(f"Marked expense #{choice} as reviewed")
            else:
                print("Invalid selection!")
    except:
        print("Error processing review")

def view_expenses(daily_exps):
    print("\nView Expenses")
    print("1. View All")
    print("2. View Unreviewed Only")
    print("3. View by Date Range")
    
    try:
        choice = input("Enter choice (1-3): ")
        expenses = daily_exps["expenses"]
        
        if choice == '2':
            expenses = [e for e in expenses if not e["reviewed"]]
        elif choice == '3':
            from datetime import datetime
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            try:
                start_date = datetime.strptime(start, "%Y-%m-%d")
                end_date = datetime.strptime(end, "%Y-%m-%d")
                expenses = [
                    e for e in expenses 
                    if start_date <= datetime.strptime(e["date"], "%Y-%m-%d") <= end_date
                ]
            except:
                print("Invalid date format!")
                return
        elif choice != '1':
            print("Invalid choice!")
            return
            
        if not expenses:
            print("\nNo expenses found!")
            return
            
        print("\nDaily Expenses:")
        print("=" * 50)
        total = 0
        for i, expense in enumerate(expenses, 1):
            status = "✓" if expense["reviewed"] else " "
            print(f"{i}. [{status}] {expense['date']}: {expense['description']} - ${expense['amount']:.2f}")
            total += expense["amount"]
        
        print("=" * 50)
        print(f"Total: ${total:.2f} | Count: {len(expenses)}")
        
    except Exception as e:
        print(f"Error: {e}")

def manage_daily_expenses(daily_exps, finance_data, user_settings):
    while True:
        print("\nDaily Expense Tracking")
        print("1. Add Expense")
        print("2. Review Expenses")
        print("3. View Expenses")
        print("4. Back to Main Menu")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            add_expense(daily_exps, finance_data)
        elif choice == '2':
            review_expenses(daily_exps)
        elif choice == '3':
            view_expenses(daily_exps)
        elif choice == '4':
            daily_expenses.save(daily_exps)
            return
        else:
            print("Invalid choice!")