from utils import clear_console, ask_int_input


def select_fight_action(player):
    from models import Action
    while True:
        clear_console()
        print("1 - Physical attack")
        print(f"2 - Cast a spell (Remaining mana points: {player.mana_points})")
        print("3 - Chat")
        user_input = ask_int_input(f"Select {player.name} next action: ")
        if user_input in [Action.CHAT.value, Action.PHYSICAL.value, Action.SPELL.value]:
            return Action(user_input)
        print("Invalid action.")
