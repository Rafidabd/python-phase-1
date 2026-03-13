from modules.storage import load_expenses,save_expenses,generate_expense_id
from modules.config_loader import load_config


def add_expense(title,amount,category,date):
    expense_data=load_expenses()
    config = load_config()
    categories = config["categories"]
    expense_id=generate_expense_id(expense_data)
    if category not in categories:
        return {"status":"error",
            "message":"invalid category"} 
    added_expenses={ "id":expense_id,
                "title":title,
                "amount":int(amount),
                "category":category,
                "date":date

                }
    expense_data.append(added_expenses)
    save_expenses(expense_data)
    return {"status":"success",
            "message":"Expense record has been added successfully"} 

def get_all_expenses():
    expenses=load_expenses()
    return expenses 



   