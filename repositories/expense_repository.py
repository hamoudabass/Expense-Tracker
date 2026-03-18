# repositories/expense_repository.py
import json
import os
from datetime import datetime

class ExpenseRepository:
    """Toutes les opérations BDD passent par ici"""

    DATA_FILE = "database/expenses.json"

    @staticmethod
    def find_all() -> list:
        if not os.path.exists(ExpenseRepository.DATA_FILE):
            return []
        with open(ExpenseRepository.DATA_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def find_by_id(expense_id: int) -> dict | None:
        expenses = ExpenseRepository.find_all()
        for e in expenses:
            if e["id"] == expense_id:
                return e
        return None

    @staticmethod
    def save(expenses: list) -> None:
        with open(ExpenseRepository.DATA_FILE, "w") as f:
            json.dump(expenses, f, indent=2)

    @staticmethod
    def update_by_id(expense_id: int, new_description: str, new_amount: float) -> bool:

        expenses = ExpenseRepository.find_all()
        filtered = [e for e in expenses if e["id"] != expense_id]

        if len(filtered) == len(expenses):
            return False
            # id introuvable

        expense = expenses[expense_id - 1]
        expense["date"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        expense["description"] = new_description
        expense["amount"] = new_amount

        ExpenseRepository.save(expenses)
        return True

    @staticmethod
    def delete_by_id(expense_id: int) -> bool:
        expenses = ExpenseRepository.find_all()
        filtered = [e for e in expenses if e["id"] != expense_id]
        if len(filtered) == len(expenses):
            return False  # id introuvable
        ExpenseRepository.save(filtered)
        return True