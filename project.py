import csv
import os

def add_expense(date, category, description, amount, filename='expenses.csv'):
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Date', 'Category', 'Description', 'Amount'])
        writer.writerow([date, category, description, amount])

def view_expense(filename='expenses.csv'):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for index,row in enumerate(reader,start=1):
                print(f"{index}.Date: {row[0]},Category: {row[1]},Description:{row[2]},Amount: ${row[3]}")
    except FileNotFoundError:
        print("No expenses found yet")


def total_expenses(filename='expenses.csv'):
    total = 0.0
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                try:
                    total += float(row[3])
                except ValueError:
                    print(f"Invalid amount value: {row[3]}")
    except FileNotFoundError:
        print("No expenses found.")
    return total

def remove_expense(row_number, filename='expenses.csv'):
    try:
        with open(filename, 'r') as file:
            rows = list(csv.reader(file))
        if 1 <= row_number <= len(rows)-1:
            del rows[row_number]
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Expense removed successfully.")
        else:
            print("Invalid row number.")
    except FileNotFoundError:
        print("No expenses found yet.")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View total expenses")
        print("4. Remove expense")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            try:
                amount = float(input("Enter the amount: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
            add_expense(date, category, description, amount)
            print("Expense added successfully.")
        elif choice == '2':
            view_expense()
        elif choice == '3':
            total = total_expenses()
            print(f"Total expenses: ${total:.2f}")
        elif choice == '4':
            view_expense()
            try:
                row_number = int(input("Enter the row to delete: "))
                remove_expense(row_number)
            except ValueError:
                print("Invalid input for row number.")
        elif choice == '5':
            print("Exit")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
