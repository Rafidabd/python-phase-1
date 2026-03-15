from modules.expense_manager import add_expense, get_all_expenses, delete_expense
from modules.display import display_expenses, display_total_expense, display_category_summary
from modules.analytics import calculate_total_expenses, category_summary, filter_by_category


def menu():

    while True:

        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Total Spending")
        print("5. Category Summary")
        print("6. Filter by Category")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            title = input("Title: ").strip()
            amount = input("Amount: ").strip()
            category = input("Category: ").strip()
            date = input("Date: ").strip()

            result = add_expense(title, amount, category, date)

            print(result["status"])
            print(result["message"])


        elif choice == "2":

            expenses = get_all_expenses()
            display_expenses(expenses)


        elif choice == "3":

            confirmation = input("Are you sure? (y/n): ").strip().lower()

            if confirmation == "y":

                expense_id = input("Enter expense ID: ").strip().upper()

                result = delete_expense(expense_id)

                print(result["status"])
                print(result["message"])

            elif confirmation == "n":
                print("Deletion cancelled.")

            else:
                print("Please enter y or n.")


        elif choice == "4":

            expenses = get_all_expenses()

            total = calculate_total_expenses(expenses)

            display_total_expense(total)


        elif choice == "5":

            expenses = get_all_expenses()

            summary = category_summary(expenses)

            display_category_summary(summary)


        elif choice == "6":

            category = input("Enter category: ").strip()

            expenses = get_all_expenses()

            result = filter_by_category(expenses, category)

            if isinstance(result, dict):
                print(result["status"])
                print(result["message"])
            else:
                display_expenses(result)


        elif choice == "7":

            print("Exiting program...")
            break

        else:
            print("Invalid option.") 