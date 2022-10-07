import os

temperatures = []


def auto_fill():
    print("Filling temperatures with random values...")
    temperatures.clear()
    import random
    for i in range(31):
        temperatures.append(random.randint(20, 40))


def fill_temperatures():
    while True:
        temp = input("Enter a temperature (or 'q' to quit): ")
        try:
            if temp == "auto":
                auto_fill()
                break
            if temp == 'q':
                break
            temp = int(temp)
            temperatures.append(temp)
            if len(temperatures) >= 31:
                break
        except ValueError:
            print("Invalid input")
            continue


def display_menu():
    os.system("clear")
    print("1 - Display maximum temperature")
    print("2 - Display minimum temperature")
    print("3 - Display average temperature")
    print("4 - Display all temperatures in ascending order")
    print("5 - Exit")
    return input("Select an action: ")


def moyenne(items):
    return sum(items) / len(items)


def liste(items):
    return sorted(items)


fill_temperatures()
while True:
    user_input = display_menu()
    if user_input == "1":
        print(f"Maximum temperature: {max(temperatures)}")
    elif user_input == "2":
        print(f"Minimum temperature: {min(temperatures)}")
    elif user_input == "3":
        print(f"Average temperature: {moyenne(temperatures)}")
    elif user_input == "4":
        print(f"All temperatures in ascending order: {liste(temperatures)}")
    elif user_input == "5":
        break
    else:
        print("Invalid input")
    input("Press enter to continue...")
