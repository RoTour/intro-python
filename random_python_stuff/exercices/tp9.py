import utils


class Corporation:
    name: str
    nb_employees: int
    turnover: float

    def __init__(self, _name, _nb_employees, _turnover):
        self.name = _name
        self.nb_employees = _nb_employees
        self.turnover = _turnover


corp_name = utils.ask_str_input("Enter the name of the corporation: ")
corp_nb_employees = utils.ask_int_input("Enter the number of employees: ")
corp_turnover = utils.ask_float_input("Enter the turnover: ")

corp = Corporation(corp_name, corp_nb_employees, corp_turnover)

print("The corporation", corp.name, "has", corp.nb_employees, "employees and a turnover of", corp.turnover, "euros.")
