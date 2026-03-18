
from controllers.expense_controller import ExpenseController

def menu():
    print('='*20,'Expenses Tracker','='*20)
    print('1. Add an expense')
    print('2. Update an expenses')
    print('3. Delete an expense')

def get_int_input(prompt: str) -> int | None:
    while True:

        value = input(prompt).strip()

        if not value:
            print("❌ Ce champ ne peut pas être vide.")
            continue

        try:
            value = int(value)
            return value

        except ValueError:
            print("❌ Veuillez entrer un nombre entier valide.")

def get_float_input(prompt: str) -> float | None:
    while True:
        value = input(prompt).strip()

        if not value:
            print("❌ Ce champ ne peut pas être vide.")
            continue

        try:
            value = float(value)
            return value
        except ValueError:
            print("❌ Veuillez entrer un nombre valide.")

def get_str_input(prompt: str) -> str | None:
    while True:
        value = input(prompt).strip()

        if not value:
            print("❌ Ce champ ne peut pas être vide.")
            continue

        try:
            float(value)  # si ça réussit → c'est un nombre
            print("❌ Ce champ ne peut pas contenir un nombre.")
        except ValueError:
            return value  # si ça échoue → c'est bien un str

if __name__ == '__main__':
    while True:
        menu()
        choice = input("Select an option(1-3) : ")
        print("="*20)

        if choice == "1":
            description = get_str_input("Description : ")
            amount = get_float_input("Amount : ")

            ExpenseController.add_expense(description, amount)


        elif choice == "2":

            id_expense = get_int_input("ID of expense : ")

            # ✅ Vérifier que l'ID existe AVANT de continuer
            if not ExpenseController.expense_exists(id_expense):
                print(f"❌ No expenses found with ID: {id_expense}.")
                continue  # ← retourne au menu directement

            description = get_str_input("New description : ")
            amount = get_float_input("New amount : ")
            ExpenseController.update_expense(id_expense, description, amount)


        elif choice == "3":
            id_expense = get_int_input("ID of expense : ")

            # ✅ Vérifier que l'ID existe AVANT de continuer
            if not ExpenseController.expense_exists(id_expense):
                print(f"❌ No expenses found with ID: {id_expense}.")
                continue  # ← retourne au menu directement

            ExpenseController.delete_expense(id_expense)

