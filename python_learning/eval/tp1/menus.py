import utils as u
from models import Action


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
            print(f"{i+1} - {personnage.name} {'(mort)' if not personnage.is_alive else ''}")
        user_input = u.ask_int_input(msg)
        if user_input > len(personnages) or user_input < 1:
            print("Numéro invalide.")
            u.wait_for_enter()
            continue
        return personnages[user_input - 1]


def afficher_choix():
    print("1 - Effectuer une action")
    print("2 - Quitter")
    return u.ask_int_input("Choisissez une option: ")