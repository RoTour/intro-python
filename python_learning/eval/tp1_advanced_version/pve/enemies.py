import random

from models import IEntity, Spell


class IEnemy(IEntity):

    def __init__(self, _name: str, _strength: int, _lives: int, _spells=None):
        super().__init__(_name, _strength, _lives)
        if _spells is None:
            _spells = []
        self.actions = _spells

    def attack(self, target):
        random_action = random.choice(list(self.actions))
        target_killed, spell_successful, inflicted_damage = self.cast_spell(target, random_action, True)
        if not spell_successful:
            print(f"{self.name} is exhausted and can't move anymore !")
        else:
            print(f"{self.name} attacks {target.name} with {random_action.name}, inflicting {inflicted_damage} damages.")
            print(f"{target.name} now has {target.strength} strength point (-{inflicted_damage}) and {target.lives} lives left")
        return target_killed, spell_successful


class Skeleton(IEnemy):
    def __init__(self, _name_suffix: str = ""):
        _default_power = 10
        _spells = [Spell("Down to the bone", _default_power, 1)]
        super().__init__(f"Skeleton {_name_suffix}", _default_power, 1, _spells)


class Orc(IEnemy):
    def __init__(self, _name_suffix: str = ""):
        _default_power = 50
        _spells = [Spell("Gnurk", _default_power, 1)]
        super().__init__(f"Orc {_name_suffix}", _default_power, 1)
