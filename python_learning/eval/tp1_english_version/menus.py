import utils as u
from models import Action, Character


def select_action(player: Character):
    while True:
        u.clear_console()
        print("1 - Physical attack")
        print(f"2 - Cast a spell (Remaining mana points: {player.mana_points})")
        print("3 - Chat")
        user_input = u.ask_int_input(f"Select {player.name} next action: ")
        if user_input in [Action.CHAT.value, Action.PHYSICAL.value, Action.SPELL.value]:
            return Action(user_input)
        print("Invalid action.")


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