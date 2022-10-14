import pandas as pd
import tp11_source.models as m

csv = pd.read_csv("resources/entreprises.csv", skiprows=1)

entreprises = []

print(csv)

for row_id, row_data in csv.iterrows():
    new_company = None
    if row_data["Type"] == "Micro Entreprise":
        new_company = m.MicroCorp(row_data["Nom"])
    elif row_data["Type"] == "PME":
        new_company = m.SmallCorp(row_data["Nom"], row_data["Employees"])
    else:
        new_company = m.BigCorp(row_data["Nom"], row_data["Employees"], row_data["Chiffre d'affaire"])
    entreprises.append(new_company)


for corp in entreprises:
    corp.display()
