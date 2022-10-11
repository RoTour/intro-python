import utils as u
from models import Action, Character, GameFeature


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


def select_game_feature():
    print("1 - Action")
    print("2 - Quit")
    return u.select_item([GameFeature.PVP.value, GameFeature.PVE.value], "Select an option: ")
