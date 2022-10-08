import utils


class Corporation:
    name: str
    nb_employees: int
    turnover: float

    def __init__(self, _name: str, _nb_employees: int, _turnover: float):
        self.name = _name
        self.nb_employees = _nb_employees
        self.turnover = _turnover

    def display(self):
        print(f"The corporation {self.name} has {self.nb_employees} employees and a turnover of {self.turnover} euros.")


nb_corps_to_create = utils.ask_int_input("Enter the number of corporations to create: ")
corps = []

for i in range(nb_corps_to_create):
    corp_name = utils.ask_str_input("Enter the name of the corporation: ")
    corp_nb_employees = utils.ask_int_input("Enter the number of employees: ")
    corp_turnover = utils.ask_float_input("Enter the turnover: ")
    corps.append(Corporation(corp_name, corp_nb_employees, corp_turnover))
    print(f"Corp {corp_name} created.\n")

for corp in corps:
    corp.display()
