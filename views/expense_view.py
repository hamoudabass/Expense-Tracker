
class ExpenseView:

    @staticmethod
    def display_add_expense(message : str) -> None:
        """Affiche un message d'ajout de la dépense"""
        print(f"\n✓ Dépense ajoutée : {message}\n")

    @staticmethod
    def display_update_expense(message: str) -> None:
        """Affiche un message de modification de la dépense"""
        print(f"\n✓ Dépense modifiée : {message}\n")

    @staticmethod
    def display_delete_expense(message : str) -> None:
        """Affiche un message de supression de la dépense"""
        print(f"\n✓ Dépense supprimée : {message}\n")

    @staticmethod
    def display_success(message):
        """Affiche un message de succès"""
        print(f"\n✓ {message}\n")

    @staticmethod
    def display_error(message):
        """Affiche un message d'erreur"""
        print(f"\n✗ Erreur: {message}\n")