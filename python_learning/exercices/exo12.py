grades = []


def add_grade(grade):
    grades.append(grade)


def get_average():
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print("No grades have been entered.")


def ask_number(str):
    while True:
        try:
            return int(input(str))
        except ValueError:
            print("Please enter a valid integer.")


def get_grade(index):
    try:
        return grades[index]
    except IndexError:
        print("This grade does not exist.")


while True:
    print("1 - Add a grade")
    print("2 - Get average")
    print("3 - Get a grade")
    print("4 - Quit")

    choice = ask_number("Select an action")

    if choice == 1:
        add_grade(ask_number("Add a grade: "))
    elif choice == 2:
        print(get_average())
    elif choice == 3:
        print(get_grade(ask_number("Enter the grade index: ")))
    elif choice == 4:
        break
    else:
        print("Invalid choice.")

    input("Press enter to continue...")
