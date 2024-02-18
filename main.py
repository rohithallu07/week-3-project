import csv
from datetime import datetime

EXPENSE_FILE = "expenses.csv"


def create_expense_file():
    with open(EXPENSE_FILE, 'a', newline='') as file:
        csv.writer(file).writerow(["Date", "Category", "Amount"])


def get_expense_data():
    with open(EXPENSE_FILE, 'r') as file:
        return list(csv.DictReader(file))


def add_expense(date, category, amount):
    with open(EXPENSE_FILE, 'a', newline='') as file:
        csv.writer(file).writerow([date, category, amount])


def display_summary(expense_data):
    total_expenses = sum(float(expense['Amount']) for expense in expense_data)
    print("\n----- Monthly Summary -----")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print("\n----- Category-wise Expenditure -----")

    categories = set(expense['Category'] for expense in expense_data)
    for category in categories:
        category_total = sum(float(expense['Amount']) for expense in expense_data if expense['Category'] == category)
        print(f"{category}: ${category_total:.2f}")


def main():
    create_expense_file()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Display Summary")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            date, category, amount = datetime.today().strftime('%Y-%m-%d'), input("Enter expense category: "), input(
                "Enter expense amount: ")
            try:
                add_expense(date, category, float(amount))
            except ValueError:
                print("Invalid amount. Please enter a valid number.")

        elif choice == '2':
            expense_data = get_expense_data()
            print("No expenses recorded yet." if not expense_data else display_summary(expense_data))

        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

