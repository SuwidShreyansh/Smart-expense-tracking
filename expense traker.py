import random

expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (DD-MM-YYYY): ")

    expense = {"amount": amount, "category": category, "date": date}
    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\n------ All Expenses ------")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']} - {exp['category']} on {exp['date']}")
    print()

def monthly_spending():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total Monthly Spending: ₹{total}\n")

def highest_expense():
    if not expenses:
        print("No data available.\n")
        return

    max_exp = max(expenses, key=lambda x: x["amount"])
    print(f"Highest Expense: ₹{max_exp['amount']} ({max_exp['category']})\n")

def remove_duplicates():
    global expenses
    unique = list({tuple(d.items()) for d in expenses})
    expenses = [dict(u) for u in unique]
    print("Duplicates removed!\n")

def kth_highest():
    k = int(input("Enter K: "))
    amounts = sorted([exp["amount"] for exp in expenses], reverse=True)

    if k <= len(amounts):
        print(f"{k}th Highest Expense: ₹{amounts[k-1]}\n")
    else:
        print("K is larger than number of expenses.\n")

def generate_random_expense():
    amount = random.randint(50, 2000)
    category = random.choice(["Food", "Travel", "Shopping", "Bills"])
    date = "19-11-2025"
    expenses.append({"amount": amount, "category": category, "date": date})
    print("Random expense added!\n")

def menu():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Spending")
        print("4. Highest Expense")
        print("5. Remove Duplicates")
        print("6. Find Kth Highest Expense")
        print("7. Generate Random Expense")
        print("8. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            monthly_spending()
        elif choice == 4:
            highest_expense()
        elif choice == 5:
            remove_duplicates()
        elif choice == 6:
            kth_highest()
        elif choice == 7:
            generate_random_expense()
        elif choice == 8:
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")

menu()
