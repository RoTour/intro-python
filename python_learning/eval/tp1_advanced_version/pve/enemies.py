from models import IEntity


class IEnemy(IEntity):
    actions = []

    def __init__(self, _name: str, _strength: int, _lives: int, _actions: list = []):
        super().__init__(_name, _strength, _lives)
        self.actions = _actions


class Skeleton(IEnemy):
    def __init__(self, _name_suffix: str = ""):
        super().__init__(f"Skeleton {_name_suffix}", 10, 1)


class Orc(IEnemy):
    def __init__(self, _name_suffix: str = ""):
        super().__init__(f"Orc {_name_suffix}", 50, 1)
