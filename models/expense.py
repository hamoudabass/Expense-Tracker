
from datetime import datetime
from repositories.expense_repository import ExpenseRepository
from exceptions.expense_exceptions import ExpenseNotFoundError, InvalidAmountError

class Expense:

    @staticmethod
    def validate(description: str, amount: float) -> None:
        if not description or description.strip() == "":
            raise ValueError("La description ne peut pas être vide.")

        if not isinstance(amount, (int, float)):
            raise TypeError("Le montant doit être un nombre.")

        if amount <= 0:
            raise ValueError("Le montant doit être supérieur à 0.")

        if amount > 1_000_000:
            raise ValueError("Le montant est trop élevé.")

    @staticmethod
    def add(description : str, amount: int | float) -> str:

        Expense.validate(description,amount)
        expenses = ExpenseRepository.find_all()
        expense = {
            "id": len(expenses) + 1,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        ExpenseRepository.save(expenses)

        return f"ID:{expense['id']} {description} — {amount}DJF"

    @staticmethod
    def update(expense_id: int,new_description : str ,new_amount : float | int) -> str:

        found = ExpenseRepository.update_by_id(expense_id,new_description,new_amount)
        if not found:
            raise ExpenseNotFoundError(f"No expenses found with ID: {expense_id}.")

        return f"(ID:{expense_id}, description: {new_description} — {new_amount}FDJ"

    @staticmethod
    def delete(expense_id: int) -> str:

        found = ExpenseRepository.delete_by_id(expense_id)
        if not found:
            print(f"Dépense #{expense_id} introuvable.")

        return f"ID:{expense_id}"

