import random
from enum import Enum


class ExperienceLevel(Enum):
    BEGINNER = "Beginner"
    MEDIUM = "Intermédiaire"
    EXPERT = "Expert"


class Action(Enum):
    PHYSICAL = 1
    SPELL = 2
    CHAT = 3


class Status(Enum):
    CONTINUE = "Continue"
    STOP = "Stop"


class CharacterType(Enum):
    MENTOR = "Mentor"
    BACHELOR = "Bachelor"


class GameFeature(Enum):
    PVP = 1
    PVE = 2
    QUIT = 3


multipliers = {
    ExperienceLevel.BEGINNER: 1,
    ExperienceLevel.MEDIUM: 1.1,
    ExperienceLevel.EXPERT: 1.25
}


class IEntity:
    lives: int
    name: str
    strength: int
    is_alive: bool = True
    spells = []
    mana_points = 5
    level: ExperienceLevel = ExperienceLevel.BEGINNER

    def __init__(self, _name: str, _strength: int, _lives: int):
        self.name = _name
        self.strength = _strength
        self.lives = _lives

    def cast_spell(self, target, spell):
        if self.mana_points < spell.mana_cost:
            print("You don't have enough mana points to cast this spell")
            return False, False
        self.mana_points -= spell.mana_cost
        return self.deal_damage(target, spell.power, spell.name), True

    def deal_damage(self, target, damage, attack_name: str = None):
        final_damage = damage * multipliers[self.level]
        target.strength -= final_damage
        if target.strength <= 0:
            target.lives -= 1
            target.strength = 25
        if target.lives <= 0:
            target.is_alive = False
            return True, final_damage
        return False, final_damage


class Character(IEntity):

    weapon: str
    experience: int = 0
    specialisation: CharacterType

    def __init__(self, _name: str, _strength: int, weapon: str, _nbLives: int = 2):
        super().__init__(_name, _strength, _nbLives)
        self.weapon = weapon

    def check_level_up(self):
        if self.experience >= 3 and self.level == ExperienceLevel.BEGINNER:
            self.level = ExperienceLevel.MEDIUM
        if self.experience >= 10 and self.level == ExperienceLevel.MEDIUM:
            self.level = ExperienceLevel.EXPERT

    def chat(self, message: str):
        print(f"{self.name} says: {message}")

    def physical_attack(self, target, power: int = None):
        if power is None:
            power = random.randint(self.strength - 5, self.strength)
        return Character.deal_damage(self, target, power), True

    def deal_damage(self, target, damage, attack_name: str = None):
        killed, final_damage = super(Character, self).deal_damage(target, damage , attack_name)
        self.experience += 1
        target.experience += 1
        self.check_level_up()
        target.check_level_up()
        attack = self.weapon if attack_name is None else "the power of " + attack_name
        if killed:
            print(f"{self.name} hits {target.name} with {self.weapon} and kills him!")
        else:
            print(f"{self.name} inflicts {final_damage} to {target.name} with {attack}. {target.name} now has {target.strength} strength point and {target.lives} lives left")
            print(f"EXP: {self.name}: {self.experience} ({self.level.value}) | {target.name}: {target.experience} ({self.level.value})")
        return killed


class Spell:
    power: float
    name: str
    mana_cost: int = 1

    def __init__(self, _name: str, _power: float, _mana_cost: int = 1):
        self.name = _name
        self.power = _power
        self.mana_cost = _mana_cost

    def __str__(self):
        return f"{self.name} (power: {self.power} | Mana cost: {self.mana_cost})"


class Mentor(Character):

    def __init__(self, _name: str, _strength: int, weapon: str):
        super().__init__(_name, _strength, weapon)
        self.spells = [
            Spell("Exam surprise", self.strength * 2, 2),
            Spell("Ytrack challenge", self.strength * 2.25, 3),
        ]
        self.specialisation = CharacterType.MENTOR


class Bachelor(Character):

    def __init__(self, _name: str, _strength: int, weapon: str):
        super().__init__(_name, _strength, weapon)
        self.spells = [
            Spell("Stack overflow", self.strength * 1.5, 2),
            Spell("Google", self.strength * 1.75, 3),
        ]
        self.specialisation = CharacterType.BACHELOR
