#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def record_expense(self, description, amount):
        self.expenses.append({"description": description, "amount": amount})

    def view_expenses(self):
        if self.expenses:
            for expense in self.expenses:
                print(f"Description: {expense['description']}, Amount: {expense['amount']}")
        else:
            print("No expenses recorded yet.")

    def calculate_total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total expenses: {total}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Record Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            tracker.record_expense(description, amount)
            print("Expense recorded.")
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.calculate_total_expenses()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

