# exceptions/expense_exceptions.py

class ExpenseError(Exception):
    """Classe mère de toutes les erreurs du projet"""
    pass

class ExpenseNotFoundError(ExpenseError):
    """Dépense introuvable"""
    pass

class InvalidAmountError(ExpenseError):
    """Montant invalide"""
    pass

class InvalidDescriptionError(ExpenseError):
    """Description invalide"""
    pass