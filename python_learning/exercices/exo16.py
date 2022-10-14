import csv

from utils import ask_int_input

temperatures = {}


def clear_csv_data():
    with open("resources/temperatures.csv", "w") as f:
        csv.writer(f).writerows([])


def write_csv_data(data: list):
    with open("resources/temperatures.csv", "a") as f:
        csv.writer(f).writerow(data)


def read_csv_data():
    with open("resources/temperatures.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            temperatures[row[0]] = int(row[1])


for i in range(3):
    temp = ask_int_input("Enter a temperature: ")
    day = ask_int_input("enter day number: ")
    month = ask_int_input("enter month number: ")
    year = 2022
    date = f"{day}/{month}/{year}"
    print(f"{date} - {temp}")
    temperatures[date] = temp

for date, temp in temperatures.items():
    write_csv_data([date, temp])

read_csv_data()
