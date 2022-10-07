from enum import Enum
import random


class Niveau(Enum):
    DEBUTANT = "Débutant"
    INTERMEDIAIRE = "Intermédiaire"
    EXPERT = "Expert"


class Action(Enum):
    PARLER = "Parler"
    ATTAQUER = "Attaquer"


class Personnage:
    nombreDeVies: int
    nom: str
    force: int
    arme: str
    niveau: Niveau
    experience: int = 0

    def __init__(self, _nom: str, _force: int, _arme: str, _nombreDeVies: int = 2, _niveau: Niveau = Niveau.DEBUTANT):
        self.nom = _nom
        self.force = _force
        self.arme = _arme
        self.nombreDeVies = _nombreDeVies
        self.niveau = _niveau

    def check_level_up(self):
        if self.experience >= 3 and self.niveau == Niveau.DEBUTANT:
            self.niveau = Niveau.INTERMEDIAIRE
        if self.experience >= 10 and self.niveau == Niveau.INTERMEDIAIRE:
            self.niveau = Niveau.EXPERT

    def parler(self, message: str):
        print(f"{self.nom} dit: {message}")

    def frapper(self, cible, puissance: int = None):
        if puissance is None:
            puissance = random.randint(self.force - 5, self.force)
        cible.force -= puissance
        if cible.force <= 0:
            cible.nombreDeVies -= 1
            cible.force = 25
        if cible.nombreDeVies <= 0:
            print(f"{self.nom} frappe {cible.nom} avec {self.arme} et l'achève!")
            return
        self.experience += 1
        cible.experience += 1
        self.check_level_up()
        cible.check_level_up()
        print(f"{self.nom} frappe {cible.nom} et lui enlève {self.force} points de vie. "
              f" (restant à {cible.nom}: Force: {cible.force}, Vies: {cible.nombreDeVies})")
        print(f"EXP: {self.nom}: {self.experience} ({self.niveau.value}) | {cible.nom}: {cible.experience} ({self.niveau.value})")

