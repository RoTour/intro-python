import utils as u
from models import Personnage, Action

def selectionner_action():
    while True:
        u.rafraichir_console()
        print("1 - Frapper")
        print("2 - Parler")
        user_input = u.ask_int_input("Entrez le numéro de l'action à effectuer: ")
        if user_input == 1:
            return Action.ATTAQUER
        elif user_input == 2:
            return Action.PARLER


def selectionner_personnage(personnages, msg: str = "Choisissez un personnage: "):
    while True:
        u.rafraichir_console()
        for i, personnage in enumerate(personnages):
            print(f"{i+1} - {personnage.nom}")
        user_input = u.ask_int_input(msg)
        if user_input > len(personnages) or user_input < 1:
            print("Numéro invalide.")
            wait_for_enter()
            continue
        return personnages[user_input - 1]