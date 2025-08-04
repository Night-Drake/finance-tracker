from datetime import datetime
from collections import defaultdict
from data import expense_data
from features.balance_management import update_balance 

def add_expense(expenses_data, finance_data):
    print("\nAvailable Categories:")
    for i, category in enumerate(expenses_data["categories"], 1):
        print(f"{i}. {category}")
    
    try:
        cat_choice = int(input("Select category (number): "))
        if cat_choice < 1 or cat_choice > len(expenses_data["categories"]):
            print("Invalid category selection!")
            return
        
        category = expenses_data["categories"][cat_choice-1]
        amount = float(input("Expense amount: $"))
        
        date_str = input("Date (YYYY-MM-DD, enter for today): ").strip()
        if not date_str:
            date_str = datetime.now().strftime("%Y-%m-%d")
        else:
            datetime.strptime(date_str, "%Y-%m-%d")
        
        if update_balance(finance_data, "cash", amount, "subtract"):
            expenses_data["expenses"].append({
                "category": category,
                "amount": amount,
                "date": date_str
            })
            print(f"Added ${amount:.2f} expense for {category} on {date_str}")
        
    except ValueError as e:
        print(f"Invalid input: {e}")

def calculate_averages(expenses_data):
    monthly_data = defaultdict(lambda: defaultdict(list))
    
    for expense in expenses_data["expenses"]:
        try:
            date = datetime.strptime(expense["date"], "%Y-%m-%d")
            month_key = date.strftime("%Y-%m")
            monthly_data[month_key][expense["category"]].append(expense["amount"])
        except:
            continue
    
    if not monthly_data:
        print("\nNo expense data available")
        return
    
    print("\nMonthly Expense Averages:")
    print("-------------------------")
    
    for month, categories in sorted(monthly_data.items()):
        print(f"\nMonth: {month}")
        print("-" * 30)
        total_month = 0
        
        for category, amounts in categories.items():
            category_total = sum(amounts)
            category_avg = category_total / len(amounts)
            total_month += category_total
            print(f"{category.capitalize():<10} | Total: ${category_total:>8.2f} | Avg: ${category_avg:>8.2f}")
        
        print("-" * 30)
        print(f"{'TOTAL':<10} | ${total_month:>8.2f}")

def manage_expenses(expenses_data, finance_data):
    while True:
        print("\nExpense Management")
        print("1. Add New Expense")
        print("2. View Monthly Averages")
        print("3. Back to Main Menu")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            add_expense(expenses_data, finance_data)
        elif choice == '2':
            calculate_averages(expenses_data)
        elif choice == '3':
            expense_data.save(expenses_data)
            return
        else:
            print("Invalid choice!")