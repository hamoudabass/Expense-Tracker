
from models.expense import Expense
from views.expense_view import ExpenseView
from exceptions.expense_exceptions import ExpenseNotFoundError
from repositories.expense_repository import ExpenseRepository

class ExpenseController:

    @staticmethod
    def expense_exists(expense_id: int) -> bool:
        expenses = ExpenseRepository.find_all()
        return any(e["id"] == expense_id for e in expenses)

    @staticmethod
    def add_expense(description, amount):
        try :
            message = Expense.add(description, amount)
            ExpenseView.display_add_expense(message)

        except Exception as e:
            ExpenseView.display_error(str(e))

    @staticmethod
    def delete_expense(id_expense):
        try :
            message = Expense.delete(id_expense)
            ExpenseView.display_delete_expense(message)
        except Exception as e:
            ExpenseView.display_error(str(e))

    @staticmethod
    def update_expense(expense_id: int,new_description : str ,new_amount : float | int):
        try:
            message = Expense.update(expense_id, new_description, new_amount)
            ExpenseView.display_update_expense(message)

        except ExpenseNotFoundError as e:

            ExpenseView.display_error(str(e))

