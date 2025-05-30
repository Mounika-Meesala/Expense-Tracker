import os
import csv
from io import StringIO
from contextlib import redirect_stdout
from project import add_expense,view_expense, total_expenses, remove_expense


filename = 'expenses.csv'

def setup():
    if os.path.isfile(filename):
        os.remove(filename)

def teardown():
    if os.path.isfile(filename):
        os.remove(filename)

def test_add_expense():
    setup()
    add_expense('2024-09-01', 'Food', 'Lunch', 15.00, filename)
    with open(filename, 'r') as file:
        rows = list(csv.reader(file))
    assert len(rows) == 2
    assert rows[1] == ['2024-09-01', 'Food', 'Lunch', '15.0']
    teardown()
def test_view_expense():
    setup()


    add_expense('01-01-2024', 'Food', 'Lunch', 15.50, filename)
    add_expense('02-01-2024', 'Transport', 'Bus Ticket', 2.75, filename)


    with StringIO() as buf, redirect_stdout(buf):
        view_expense(filename)
        output = buf.getvalue().strip()


    expected_output = (
        "1.Date: 01-01-2024,Category: Food,Description:Lunch,Amount: $15.5\n"
        "2.Date: 02-01-2024,Category: Transport,Description:Bus Ticket,Amount: $2.75"
    )

    assert output == expected_output, f"Expected:\n{expected_output}\nGot:\n{output}"
    teardown()


def test_total_expenses():
    setup()
    add_expense('2024-09-02', 'Transport', 'Bus fare', 2.50, filename)
    add_expense('2024-09-03', 'Entertainment', 'Movie', 20.00, filename)
    total = total_expenses(filename)
    assert total == 22.50
    teardown()

def test_remove_expense():
    setup()
    add_expense('2024-09-04', 'Utilities', 'Electric Bill', 60.00, filename)
    add_expense('2024-09-05', 'Food', 'Dinner', 25.00, filename)
    remove_expense(2, filename)
    with open(filename, 'r') as file:
        rows = list(csv.reader(file))
    assert len(rows) == 2
    assert rows[1] == ['2024-09-04','Utilities','Electric Bill','60.0']


def main():
    test_add_expense()
    test_total_expenses()
    test_remove_expense()
    test_view_expense()
    print("All tests passed.")

if __name__ == "__main__":
    main()
