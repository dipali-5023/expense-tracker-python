import sqlite3

# connect to database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT,
category TEXT,
amount REAL,
description TEXT
)
""")

conn.commit()

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    cursor.execute(
        "INSERT INTO expenses(date,category,amount,description) VALUES (?,?,?,?)",
        (date,category,amount,description)
    )

    conn.commit()
    print("Expense added successfully!")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    print("\nExpense List\n")
    for row in rows:
        print(row)

def delete_expense():
    expense_id = input("Enter expense ID to delete: ")

    cursor.execute(
        "DELETE FROM expenses WHERE id=?",
        (expense_id,)
    )

    conn.commit()
    print("Expense deleted!")

def expense_summary():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print("\nTotal Expenses:", total)

def category_report():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()

    print("\nExpense by Category")
    for row in rows:
        print(row[0], ":", row[1])

while True:
    print("\nExpense Tracker")
    print("1 Add Expense")
    print("2 View Expenses")
    print("3 Delete Expense")
    print("4 Expense Summary")
    print("5 Category Report")
    print("6 Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        expense_summary()

    elif choice == "5":
        category_report()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice")