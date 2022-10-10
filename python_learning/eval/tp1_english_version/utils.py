import os


def ask_int_input(text, error_message="Please enter a valid integer."):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print(error_message)


def ask_float_input(text, error_message="Please enter a valid float."):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print(error_message)


def ask_str_input(text, error_message="Please enter a valid string."):
    while True:
        try:
            return str(input(text))
        except ValueError:
            print(error_message)


def clear_console():
    os.system("clear")


def wait_for_enter():
    input("Press enter to continue...")


def select_item(items, msg: str = "Select an item: "):
    while True:
        clear_console()
        for i, item in enumerate(items):
            print(f"{i+1} - {item}")
        user_input = ask_int_input(msg)
        if user_input > len(items) or user_input < 1:
            print("Invalid item.")
            wait_for_enter()
            continue
        return items[user_input - 1]