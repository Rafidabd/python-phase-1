
def display_expenses(expenses_list):

    if not expenses_list:
        print("No expenses recorded yet.")
        return

    print("========== Expense List ==========")

    print(f"{'ID':>8} {'Title':<18} {'Amount':>8} {'Category':<18} {'Date':>10}")
    print("-"*60)

    for expense in expenses_list:
        print(
            f"{expense['id']:>8} "
            f"{expense['title']:<18} "
            f"{expense['amount']:>8} "
            f"{expense['category']:<18} "
            f"{expense['date']:>10}"
        )

    print() 