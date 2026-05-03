from utils import add_transaction, view_transactions, show_summary

def main():
    while True:
        print("\n--- EXPENSE TRACKER MENU ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. View Summary")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")

        if choice in ["1", "2"]:
            date = input("Date (YYYY-MM-DD): ")
            cat = input("Category (e.g., Food, Rent, Salary): ")
            desc = input("Description: ")
            amt = input("Amount: ")
            t_type = "Income" if choice == "1" else "Expense"
            add_transaction(date, cat, desc, amt, t_type)

        elif choice == "3":
            view_transactions()

        elif choice == "4":
            show_summary()

        elif choice == "5":
            print("Closing tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
