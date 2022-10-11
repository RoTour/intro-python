from models import Character, Action
import utils as u

def select_pvp_action(player: Character):
    while True:
        u.clear_console()
        print("1 - Physical attack")
        print(f"2 - Cast a spell (Remaining mana points: {player.mana_points})")
        print("3 - Chat")
        user_input = u.ask_int_input(f"Select {player.name} next action: ")
        if user_input in [Action.CHAT.value, Action.PHYSICAL.value, Action.SPELL.value]:
            return Action(user_input)
        print("Invalid action.")
