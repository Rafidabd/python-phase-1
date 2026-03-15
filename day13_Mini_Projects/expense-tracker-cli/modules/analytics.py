from modules.config_loader import load_config


def calculate_total_expenses(expenses):

    total = 0

    for expense in expenses:
        total += int(expense["amount"])

    return total


def category_summary(expenses):

    summary = {}

    for expense in expenses:

        category = expense["category"]
        amount = int(expense["amount"])

        if category not in summary:
            summary[category] = 0

        summary[category] += amount

    return summary


def filter_by_category(expenses, category):

    config = load_config()

    if category not in config["categories"]:
        return {
            "status": "error",
            "message": "Invalid category"
        }

    filtered_expenses = []

    for expense in expenses:
        if expense["category"] == category:
            filtered_expenses.append(expense)

    return filtered_expenses  
            
    
    



