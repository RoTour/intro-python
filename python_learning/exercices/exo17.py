import pandas as pd


csv = pd.read_csv("resources/entreprises.csv", skiprows=1)

# print column Nom from csv

# print(csv["Nom"])


csv_dict = csv.to_dict()

for row_id in csv_dict["Nom"]:
    print(csv_dict["Nom"][row_id])

for row_id, row_data in csv.iterrows():
    print(row_data["Nom"])
