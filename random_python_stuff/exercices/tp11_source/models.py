from enum import Enum


class CorpType(Enum):
    MICRO = "Micro"
    SMALL = "Small"
    BIG = "Big"


class Corp:
    name: str

    def __init__(self, _name: str):
        self.name = _name

    def display(self):
        print(f"Corporation name: {self.name}.")


class MicroCorp(Corp):
    corp_type = "Micro Corporation"


class SmallCorp(Corp):
    corp_type = "Small Corporation"
    nb_employees: int

    def __init__(self, _name: str, _nb_employees: int):
        super().__init__(_name)
        self.nb_employees = _nb_employees

    def display(self):
        super().display()
        print(f"Number of employees: {self.nb_employees}.")


class BigCorp(Corp):
    corp_type = "Big Corporation"
    nb_employees: int
    turnover: float

    def __init__(self, _name: str, _nb_employees: int, _turnover: float):
        super(BigCorp, self).__init__(_name)
        self.nb_employees = _nb_employees
        self.turnover = _turnover

    def display(self):
        super().display()
        print(f"Number of employees: {self.nb_employees}; Turnover: {self.turnover}.")
