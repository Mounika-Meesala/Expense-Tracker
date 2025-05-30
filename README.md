# __Expense Tracker__

## __Video demo__:https://youtu.be/zS0Z6Grz_CQ

### __Description__:
This is a simple expense tracker program that allows you manage your daily expenses.<br/>
You can add,view,calculate the total of all your expenses and remove your expenses using this program.<br/>
This data is stored in a CSV file,making it easy to track and review  later.

## __Features__:
1.Add an expense: Enter the date,category,description,and amount of the expense.<br/>
2.View an expense: Displays all stored expenses in a structured format.<br/>
3.Remove an expense: Remove an expense by selecting its row number.<br/>
4.View total expenses: Calculate and displays the total of all expenses.<br/>
5.Exit: safely exits the program.

## __Functions__:

1.**add_expense(date, category, description, amount)**:<br/>
  -Appends a new expense to a CSV file(expenses.csv)<br/>
  -If the file doesn't exist,it creates one with headers: Date,Category,Description,Amount.

2.**view_expense()**:<br/>
  -Reads and prints all the expenses stored in the expenses.csv file.<br/>
  -Handles and case where no file exists or no expenses are recorded.

3.**total_expenses()**:<br/>
  -Calculates and returns the total amount of all expenses.<br/>
  -If the file does not exist, it informs the user.

4.**remove_expense(row_number)**:<br/>
  -Delets a specific expense entry by row number from the expenses.csv file.<br/>
  -Ensures the selected row exists and provides feedback on succesful deletion.

## __How to Run__:
  -Save the script as project.py.<br/>
  -Run the script using:<br/>
  ```bash
       python project.py
  ```

## __CSV File structure__:
  -The program stores the data in a CSV file named expenses.csv.<br/>
  -The file includes the following fields.<br/>
  -*Date*: The date of the expense(in yyyy-mm-dd format).<br/>
  -*Category*: The category (e.g.,Travel,Food,Clothes,etc.).<br/>
  -*Description*: A short description of the expense.<br/>
  -*Amount*: The amount spent(in numeric form).

## __Notes__:
  -Ensure you enter the date in the correct format(yyyy-mm-dd).<br/>
  -Only valid numbers should be entered for the amount.<br/>
  -The program stores the expenses in a CSV file called expenses.csv.<br/>
  -Ensure that any entered expense amounts are valid numerical values.<br/>
  -Use option 5 to exit the program.

