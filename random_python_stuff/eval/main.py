from models import Personnage, Action
import utils as u
import menus

robin = Personnage("Robin", 25, "Gourde", 3)
# lucas = Personnage("Lucas", 25, "épée", 3)
#
# robin.frapper(lucas, 30)
# robin.frapper(lucas, 30)
# robin.frapper(lucas, 30)

personnages = [robin]


def afficher_choix():
    print("1 - Créer un personnage")
    print("2 - Effectuer une action")
    print("3 - Quitter")
    return u.ask_int_input("Choisissez une option: ")


def creer_personnage():
    u.rafraichir_console()
    nouveau_personnage = Personnage(
        u.ask_str_input("Entrez le nom du personnage: "),
        u.ask_int_input("Entrez la force du personnage: "),
        u.ask_str_input("Entrez l'arme du personnage: ")
    )
    personnages.append(nouveau_personnage)
    print(f"Le personnage {nouveau_personnage.nom} a été créé avec succès.")
    u.wait_for_enter()


def attaquer():
    personnage_a_utiliser = menus.selectionner_personnage(personnages, "Choisissez le personnage qui va attaquer: ")
    personnage_cible = menus.selectionner_personnage(personnages, "Choisissez le personnage à attaquer: ")
    personnage_a_utiliser.frapper(personnage_cible)
    u.wait_for_enter()


def parler():
    personnage_a_utiliser = menus.selectionner_personnage(personnages, "Choisissez le personnage qui va parler: ")
    personnage_a_utiliser.parler(u.ask_str_input("Entrez le message à dire: "))
    u.wait_for_enter()


def main():
    while True:
        u.rafraichir_console()
        user_input = afficher_choix()
        if user_input == 1:
            creer_personnage()
        elif user_input == 2:
            action = menus.selectionner_action()
            if action == Action.ATTAQUER:
                attaquer()
            elif action == Action.PARLER:
                parler()
            else:
                print("Action invalide.")
                u.wait_for_enter()
        else:
            return


main()
