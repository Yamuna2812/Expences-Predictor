import csv
import os

FILE_NAME = "data.csv"

def add_transaction(date, category, desc, amount, entry_type):
    # Ensure file exists with headers first
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount", "Type"])
            print("transaction added!")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, desc, amount, entry_type])
    print(f"\nSuccessfully added {entry_type}!")

def view_transactions():
    if not os.path.exists(FILE_NAME):
        print("\nNo transactions found.")
        return
    print("\n--- ALL TRANSACTIONS ---")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    
def show_summary():
    if not os.path.exists(FILE_NAME):
        print("\nNo data available.")
        return
    income = 0
    expense = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                amount = float(row["Amount"])
                if row["Type"] == "Income":
                    income += amount
                else:
                    expense += amount
            except:
                continue
            print(f"{row[0]}|{row[1]}|{row[2]}|{row[3]}|{row[4]}")
    
    print("\n--- SUMMARY ---")
    print(f"Total Income:  {income}")
    print(f"Total Expense: {expense}")
    print(f"Net Balance:   {(income - expense)}")
