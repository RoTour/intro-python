import random

import utils as u
from enums import ExperienceLevel, CharacterType, Action
from menus import select_target

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

    def cast_spell(self, target, spell, hide_text=False):
        spell_successful = False
        target_killed = False
        final_damages = 0
        if self.mana_points < spell.mana_cost and not hide_text:
            print("You don't have enough mana points to cast this spell")
            return target_killed, spell_successful, final_damages
        self.mana_points -= spell.mana_cost
        target_killed, final_damages = self.deal_damage(target, spell.power, spell.name)
        spell_successful = True
        return target_killed, spell_successful, final_damages

    def deal_damage(self, target, damage, attack_name: str = None):
        target_killed = False
        final_damage = damage * multipliers[self.level]
        target.strength -= final_damage
        if target.strength <= 0:
            target.lives -= 1
            target.strength = 25
        if target.lives <= 0:
            target.is_alive = False
            target_killed = True
        return target_killed, final_damage


class Character(IEntity):
    weapon: str
    experience: int = 0
    specialisation: CharacterType

    instances = []

    def __init__(self, _name: str, _strength: int, weapon: str, _nbLives: int = 2):
        super().__init__(_name, _strength, _nbLives)
        self.weapon = weapon
        Character.instances.append(self)

    def check_level_up(self):
        if self.experience >= 3 and self.level == ExperienceLevel.BEGINNER:
            self.level = ExperienceLevel.MEDIUM
        if self.experience >= 10 and self.level == ExperienceLevel.MEDIUM:
            self.level = ExperienceLevel.EXPERT

    def chat(self):
        print(u.ask_str_input("Enter the message to say: "))
        u.wait_for_enter()

    def physical_attack(self, target, power: int = None):
        if power is None:
            power = random.randint(self.strength - 5, self.strength)
        return Character.deal_damage(self, target, power), True

    def deal_damage(self, target, damage, attack_name: str = None):
        killed, final_damage = super(Character, self).deal_damage(target, damage, attack_name)
        self.experience += 1
        self.check_level_up()
        if issubclass(type(target), Character):
            target.experience += 1
            target.check_level_up()
        attack = self.weapon if attack_name is None else "the power of " + attack_name
        if killed:
            print(f"{self.name} kills {target.name} with {attack}!")
        else:
            print(
                f"{self.name} inflicts {final_damage} to {target.name} with {attack}. {target.name} now has {target.strength} strength point and {target.lives} lives left")
            print(
                f"EXP: {self.name}: {self.experience} ({self.level.value}) | {target.name}: {target.experience} ({self.level.value})")
        return killed, final_damage

    def attack(self, action_type: Action, available_targets=None):
        if available_targets is None:
            available_targets = Character.instances
        target = select_target(
            available_targets,
            f"{self.name}, choose your target: "
        )
        action = None
        if action_type == Action.PHYSICAL:
            action = self.physical_attack
        if action_type == Action.SPELL:
            action = self.cast_spell

        while True:
            target_killed, attack_successful, _ = action(target) if action_type == Action.PHYSICAL \
                else action(
                target,
                u.select_item(self.spells, f"(Mana points: {self.mana_points}) | Select a spell: ")
            )
            if attack_successful:
                break
            u.wait_for_enter()

        if target_killed and issubclass(type(target), Character):
            Character.instances.remove(target)
        elif target_killed:
            available_targets.remove(target)

        u.wait_for_enter()
        return target_killed


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
