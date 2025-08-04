def display_balance(data):
    print("\nCurrent Balance:")
    print(f"Total: ${data['total']:.2f}")
    print(f"Bank Card: ${data['bank_card']:.2f}")
    print(f"Cash: ${data['cash']:.2f}")

def update_balance(data, category, amount, operation):
    """Update balance for a specific category with validation"""
    if category not in data:
        print(f"Error: Invalid category '{category}'!")
        return False
        
    if operation == "add":
        data[category] += amount
        data["total"] += amount
        print(f"Added ${amount:.2f} to {category}")
        return True
        
    elif operation == "subtract":
        if data[category] < amount:
            print(f"Error: Not enough funds in {category}!")
            return False
            
        data[category] -= amount
        data["total"] -= amount
        print(f"Subtracted ${amount:.2f} from {category}")
        return True
        
    print(f"Error: Invalid operation '{operation}'!")
    return False

def add_money(data):
    print("\nAdd Money To:")
    print("1. Bank Card")
    print("2. Cash")
    account_choice = input("Select account (1-2): ")
    
    try:
        amount = float(input("Amount to add: $"))
        if amount <= 0:
            print("Amount must be positive!")
            return
    except ValueError:
        print("Invalid amount!")
        return
        
    if account_choice == '1':
        update_balance(data, "bank_card", amount, "add")
    elif account_choice == '2':
        update_balance(data, "cash", amount, "add")
    else:
        print("Invalid choice!")

def subtract_money(data):
    print("\nSubtract Money From:")
    print("1. Bank Card")
    print("2. Cash")
    account_choice = input("Select account (1-2): ")
    
    try:
        amount = float(input("Amount to subtract: $"))
        if amount <= 0:
            print("Amount must be positive!")
            return
    except ValueError:
        print("Invalid amount!")
        return
        
    if account_choice == '1':
        update_balance(data, "bank_card", amount, "subtract")
    elif account_choice == '2':
        update_balance(data, "cash", amount, "subtract")
    else:
        print("Invalid choice!")