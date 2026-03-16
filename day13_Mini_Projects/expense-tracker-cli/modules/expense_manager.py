from modules.storage import load_expenses, save_expenses, generate_expense_id
from modules.config_loader import load_config
from datetime import datetime


def add_expense(title, amount, category, date):

    expenses = load_expenses()

    config = load_config()
    categories = config["categories"]

    # Title validation
    if not title:
        return {
            "status": "error",
            "message": "Title cannot be empty"
        }

    # Amount validation
    try:
        amount = int(amount)
        if amount <= 0:
            return {
                "status": "error",
                "message": "Amount must be greater than 0"
            }
    except ValueError:
        return {
            "status": "error",
            "message": "Invalid amount"
        }

    # Category validation
    if category not in categories:
        return {
            "status": "error",
            "message": "Invalid category"
        }

    # Date validation (YYYY-MM-DD)
    try:
        datetime.strptime(date, "%Y-%m-%d") 
    except ValueError:
        return {
            "status": "error",
            "message": "Invalid date format. Use YYYY-MM-DD"
        }

    expense_id = generate_expense_id(expenses)

    new_expense = {
        "id": expense_id,
        "title": title,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(new_expense)

    save_expenses(expenses)

    return {
        "status": "success",
        "message": "Expense record has been added successfully"
    }


def get_all_expenses():

    return load_expenses()


def delete_expense(expense_id):

    expenses = load_expenses()

    for expense in expenses:

        if expense["id"] == expense_id:

            expenses.remove(expense)

            save_expenses(expenses)

            return {
                "status": "success",
                "message": f"Expense {expense_id} deleted successfully"
            }

    return {
        "status": "error",
        "message": "Expense ID not found"
    }




   