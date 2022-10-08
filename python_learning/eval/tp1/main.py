from models import Personnage, Action, Status
import utils as u
import menus

# All variables and functions in this program are in french for consistency with the required attributes and methods
# from the "Personnage" class.

personnages = []


def creer_personnage():
    u.rafraichir_console()
    nouveau_personnage = Personnage(
        u.ask_str_input(f"Entrez le nom du personnage {len(personnages)+1}: "),
        u.ask_int_input("Entrez la force du personnage: "),
        u.ask_str_input("Entrez l'arme du personnage: ")
    )
    personnages.append(nouveau_personnage)
    print(f"Le personnage {nouveau_personnage.nom} a été créé avec succès.")
    u.wait_for_enter()


def attaquer(attaquant):
    personnage_cible = menus.selectionner_personnage(
        personnages,
        f"{attaquant.nom}, choisissez le personnage à attaquer: "
    )
    cible_est_tuee = attaquant.frapper(personnage_cible)
    if cible_est_tuee:
        personnages.remove(personnage_cible)
    u.wait_for_enter()


def parler():
    personnage_a_utiliser = menus.selectionner_personnage(personnages, "Choisissez le personnage qui va parler: ")
    personnage_a_utiliser.parler(u.ask_str_input("Entrez le message à dire: "))
    u.wait_for_enter()


def gestion_creation_personnages():
    nb_joueurs = u.ask_int_input("Entrez le nombre de joueurs: ")
    for i in range(nb_joueurs):
        creer_personnage()


def tour_de_jeu(personnage):
    print(f"Tour de {personnage.nom}")
    print(f"Personnages restants: {', '.join([personnage.nom for personnage in personnages])}")
    choix = menus.afficher_choix()
    if choix == 1:
        action = menus.selectionner_action()
        if action == Action.ATTAQUER:
            attaquer(personnage)
        elif action == Action.PARLER:
            parler()
        return Status.CONTINUE
    elif choix == 2:
        return Status.STOP


def main():
    gestion_creation_personnages()
    joueur_en_cours = 0
    while len(personnages) > 1:
        u.rafraichir_console()
        status = tour_de_jeu(personnages[joueur_en_cours])
        if status is Status.STOP:
            print("Arret du jeu...")
            return
        joueur_en_cours += 1
        if joueur_en_cours >= len(personnages):
            joueur_en_cours = 0
    print(f"{personnages[0].nom} à gagné !")


main()
