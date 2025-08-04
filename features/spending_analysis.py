from datetime import datetime, timedelta
from collections import defaultdict

def analyze(daily_exps, settings):
    today = datetime.now().date()
    last_month_start = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
    last_month_end = today.replace(day=1) - timedelta(days=1)
    
    last_month_expenses = []
    for expense in daily_exps["expenses"]:
        try:
            exp_date = datetime.strptime(expense["date"], "%Y-%m-%d").date()
            if last_month_start <= exp_date <= last_month_end:
                last_month_expenses.append(expense)
        except:
            continue
    
    if not last_month_expenses:
        print("\nNo expenses found for last month!")
        return
    
    categorized = defaultdict(lambda: {"total": 0.0, "count": 0})
    for expense in last_month_expenses:
        desc = expense["description"]
        categorized[desc]["total"] += expense["amount"]
        categorized[desc]["count"] += 1
    
    sorted_expenses = sorted(categorized.items(), 
                            key=lambda x: x[1]["total"], 
                            reverse=True)
    
    print(f"\nSpending Analysis for {last_month_start.strftime('%B %Y')}:")
    print("=" * 70)
    print(f"{'Category':<25} {'Total':>10} {'Transactions':>12} {'Avg/Trans':>12} {'Warning':>10}")
    print("=" * 70)
    
    warnings = []
    monthly_income = settings.get("monthly_income", 3000)
    total_spent = sum(expense["amount"] for expense in last_month_expenses)
    
    for desc, data in sorted_expenses:
        avg = data["total"] / data["count"] if data["count"] > 0 else 0
        
        warning = ""
        for category, thresh in settings["warning_thresholds"].items():
            if category in desc:
                if data["total"] > thresh:
                    warning = "HIGH!"
                    warnings.append(f"⚠️ '{desc}' spending (${data['total']:.2f}) exceeds ${thresh} threshold")
                break
        
        if not warning and data["total"] > settings["warning_thresholds"]["other"]:
            warning = "HIGH!"
            warnings.append(f"⚠️ Uncategorized '{desc}' spending (${data['total']:.2f}) exceeds ${settings['warning_thresholds']['other']} threshold")
        
        if data["count"] > 15:
            warning = "FREQ!" if not warning else warning + "+FREQ"
            warnings.append(f"⚠️ High frequency: '{desc}' has {data['count']} transactions")
        
        print(f"{desc:<25} ${data['total']:>9.2f} {data['count']:>12} ${avg:>11.2f} {warning:>10}")
    
    spending_percentage = (total_spent / monthly_income) * 100
    if spending_percentage > 80:
        warnings.append(f"🚨 CRITICAL: Spent {spending_percentage:.1f}% of income!")
    elif spending_percentage > 60:
        warnings.append(f"⚠️ WARNING: Spent {spending_percentage:.1f}% of income")
    
    if warnings:
        print("\n" + "=" * 70)
        print("SPENDING WARNINGS:")
        for warning in warnings:
            print(warning)
    
    print("=" * 70)
    print(f"Total Spent: ${total_spent:.2f} | Monthly Income: ${monthly_income:.2f} | Percentage: {spending_percentage:.1f}%")