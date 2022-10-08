import utils as u
from models import Action


def select_action():
    while True:
        u.clear_console()
        print("1 - Attack")
        print("2 - Char")
        user_input = u.ask_int_input("Select your next action")
        if user_input == 1:
            return Action.ATTACK
        elif user_input == 2:
            return Action.CHAT


def select_player(players, msg: str = "Select a player: "):
    while True:
        u.clear_console()
        for i, personnage in enumerate(players):
            print(f"{i+1} - {personnage.name} {'(dead)' if not personnage.is_alive else ''}")
        user_input = u.ask_int_input(msg)
        if user_input > len(players) or user_input < 1:
            print("Invalid player.")
            u.wait_for_enter()
            continue
        return players[user_input - 1]


def display_choices():
    print("1 - Action")
    print("2 - Quit")
    return u.ask_int_input("Select an option: ")