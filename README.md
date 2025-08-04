A robust Python application for intelligent financial management with dual tracking systems.

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 💰 **Balance Tracking** | Monitor cash, bank, and total balances |
| 🏛 **Bill Management** | Track recurring payments without deductions |
| 🛒 **Expense Tracking** | Record daily spends with auto-deduction |
| 📈 **Analytics** | Spending insights with custom alerts |



## 📂 Project Structure

finance-tracker/
├── data/               # JSON data stores

│   ├── finance_data.json    # Balance data

│   ├── expenses_data.json   # Bill records

│   └── daily_expenses.json  # Spend logs

├── features/           # Core modules

│   ├── balance.py      # Fund management

│   ├── bills.py        # Payment tracking

│   └── analytics.py    # Insights engine

└── main.py             # Application entry


```bash
# Clone & run
git clone https://github.com/Night-Drake/finance-tracker
cd finance-tracker
python main.py
