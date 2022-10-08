import random
from enum import Enum


class ExperienceLevel(Enum):
    BEGINNER = "Beginner"
    MEDIUM = "Intermédiaire"
    EXPERT = "Expert"


class Action(Enum):
    CHAT = "Chat"
    ATTACK = "Attack"


class Status(Enum):
    CONTINUE = "Continue"
    STOP = "Stop"


multipliers = {
    ExperienceLevel.BEGINNER: 1,
    ExperienceLevel.MEDIUM: 1.1,
    ExperienceLevel.EXPERT: 1.25
}


class Character:
    lives: int
    name: str
    strength: int
    weapon: str
    level: ExperienceLevel
    is_alive: bool = True
    experience: int = 0

    def __init__(self, _nom: str, _force: int, _arme: str, _nombreDeVies: int = 2, _niveau: ExperienceLevel = ExperienceLevel.BEGINNER):
        self.name = _nom
        self.strength = _force
        self.weapon = _arme
        self.lives = _nombreDeVies
        self.level = _niveau

    def check_level_up(self):
        if self.experience >= 3 and self.level == ExperienceLevel.BEGINNER:
            self.level = ExperienceLevel.MEDIUM
        if self.experience >= 10 and self.level == ExperienceLevel.MEDIUM:
            self.level = ExperienceLevel.EXPERT

    def chat(self, message: str):
        print(f"{self.name} says: {message}")

    def attack(self, target, power: int = None):
        if power is None:
            power = random.randint(self.strength - 5, self.strength)
        target.strength -= power * multipliers[self.level]
        if target.strength <= 0:
            target.lives -= 1
            target.strength = 25
        if target.lives <= 0:
            print(f"{self.name} hits {target.name} with {self.weapon} and kills him!")
            target.is_alive = False
            return True
        self.experience += 1
        target.experience += 1
        self.check_level_up()
        target.check_level_up()
        print(f"{self.name} hits {target.name} with {self.weapon}. He has {target.strength} strength point and {target.lives} left")
        print(
            f"EXP: {self.name}: {self.experience} ({self.level.value}) | {target.name}: {target.experience} ({self.level.value})")
        return False
