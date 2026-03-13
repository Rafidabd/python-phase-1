from modules.expense_manager import add_expense, get_all_expenses,delete_expense
from modules.display import display_expenses


def menu():

    while True:

        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1": 
            title=input("Title: ").strip()
            amount=input("Amount: ").strip()
            
            category=input("Category: ").strip()
            date=input("Date: ").strip()
            added_expense_result=add_expense(title,amount,category,date)
            print(added_expense_result["status"])
            print(added_expense_result["message"]) 

        
        elif choice == "2":
            expenses = get_all_expenses()
            display_expenses(expenses)

        elif choice == "3":
            confirmation=input("Are you sure?(y/n)").strip().lower()
            if confirmation=='y':
                expense_id=input("Please enter the expense id:").strip().upper()
                deletion=delete_expense(expense_id)
                print(deletion["status"])
                print(deletion["message"])
            elif confirmation=='n':
                print("deletion cancelled")
            else:
                print("please enter a valid option(y/n)") 
 

            

            

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid option.") 