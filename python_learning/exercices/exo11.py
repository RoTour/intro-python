import os

import tp11_source.models as m
import utils as u

corps = []
while True:
    new_corp = u.ask_str_input("Enter the type of the corporation  (Micro, Small, Big): ")
    if new_corp == "q":
        break
    if new_corp == str(m.CorpType.BIG.value) or\
            new_corp == m.CorpType.SMALL.value or\
            new_corp == m.CorpType.MICRO.value:
        if new_corp == m.CorpType.BIG.value:
            new_corp = m.BigCorp(
                u.ask_str_input("Enter the name of the corporation: "),
                u.ask_int_input("Enter the number of employees: "),
                u.ask_float_input("Enter the turnover: ")
            )
        elif new_corp == m.CorpType.SMALL.value:
            new_corp = m.SmallCorp(
                u.ask_str_input("Enter the name of the corporation: "),
                u.ask_int_input("Enter the number of employees: ")
            )
        else:
            new_corp = m.MicroCorp(u.ask_str_input("Enter the name of the corporation: "))

        print("Created corp: ")
        new_corp.display()
        corps.append(new_corp)
    else:
        print("Invalid type.")

os.system("clear")
print('Recap: ')
for corp in corps:
    corp.display()
