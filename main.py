from data import finance_data, expense_data, daily_expenses, settings
from features import balance_management, expense_tracking, daily_expense_tracking, spending_analysis, settings_manager

def main():
    
    finance = finance_data.initialize()
    expenses = expense_data.initialize()
    daily_exps = daily_expenses.initialize()
    user_settings = settings.initialize()
    
    while True:
        print("\nPersonal Finance Tracker")
        print("1. View Balance")
        print("2. Add Money")
        print("3. Subtract Money")
        print("4. Expense Management (Bills)")
        print("5. Daily Expense Tracking")
        print("6. Spending Analysis")
        print("7. Settings")
        print("8. Save & Exit")
        
        choice = input("Enter choice (1-8): ")
        
        if choice == '1':
            balance_management.display_balance(finance)

        elif choice == '2':
            balance_management.add_money(finance)

        elif choice == '3':
            balance_management.subtract_money(finance)

        elif choice == '4':
            expense_tracking.manage_expenses(expenses, finance)

        elif choice == '5':
            daily_expense_tracking.manage_daily_expenses(daily_exps, finance, user_settings)

        elif choice == '6':
            spending_analysis.analyze(daily_exps, user_settings)

        elif choice == '7':
            settings_manager.configure(user_settings)

        elif choice == '8':
            finance_data.save(finance)
            expense_data.save(expenses)
            daily_expenses.save(daily_exps)
            settings.save(user_settings)
            print("All data saved. Exiting program.")
            break
        
        else:
            print("Invalid choice! Please enter 1-8.")

if __name__ == "__main__":
    main()