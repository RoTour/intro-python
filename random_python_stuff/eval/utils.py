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


def rafraichir_console():
    os.system("clear")


def wait_for_enter():
    input("Appuyez sur Entrée pour continuer...")