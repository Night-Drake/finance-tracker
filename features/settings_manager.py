from data import settings

def configure(settings_data):
    while True:
        print("\nSettings Configuration")
        print("1. Set Monthly Income")
        print("2. Set Warning Thresholds")
        print("3. View Current Settings")
        print("4. Back to Main Menu")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            try:
                income = float(input("Enter monthly income: $"))
                settings_data["monthly_income"] = income
                print("Income updated!")
            except ValueError:
                print("Invalid amount!")
        
        elif choice == '2':
            print("\nCurrent Thresholds:")
            for cat, thresh in settings_data["warning_thresholds"].items():
                print(f"{cat.capitalize()}: ${thresh:.2f}")
            
            print("\n1. Edit threshold")
            print("2. Add new category")
            sub_choice = input("Select option (1-2): ")
            
            if sub_choice == '1':
                print("\nCategories:")
                for i, cat in enumerate(settings_data["warning_thresholds"].keys(), 1):
                    print(f"{i}. {cat}")
                cat_choice = input("Select category number: ")
                
                try:
                    cat_idx = int(cat_choice) - 1
                    categories = list(settings_data["warning_thresholds"].keys())
                    if 0 <= cat_idx < len(categories):
                        category = categories[cat_idx]
                        new_thresh = float(input(f"New threshold for {category}: $"))
                        settings_data["warning_thresholds"][category] = new_thresh
                        print("Threshold updated!")
                    else:
                        print("Invalid selection!")
                except:
                    print("Invalid input!")
            
            elif sub_choice == '2':
                new_cat = input("New category name: ").strip().lower()
                if new_cat:
                    try:
                        new_thresh = float(input("Warning threshold: $"))
                        settings_data["warning_thresholds"][new_cat] = new_thresh
                        print("New category added!")
                    except ValueError:
                        print("Invalid amount!")
                else:
                    print("Category name required!")
        
        elif choice == '3':
            print("\nCurrent Settings:")
            print(f"Monthly Income: ${settings_data.get('monthly_income', 0):.2f}")
            print("Warning Thresholds:")
            for cat, thresh in settings_data["warning_thresholds"].items():
                print(f"  {cat.capitalize()}: ${thresh:.2f}")
        
        elif choice == '4':
            settings.save(settings_data)
            return
        
        else:
            print("Invalid choice!")