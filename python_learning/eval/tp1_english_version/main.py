from models import Character, Action, Status, Mentor, Bachelor
import utils as u
import menus

# All variables and functions in this program are in french for consistency with the required attributes and methods
# from the "Personnage" class.

players = [
    Mentor("Robin", 25, "Gourd"),
    Bachelor("Lucas", 25, "Cringe"),
    Bachelor("Anthony", 25, "Poison"),
]


def create_player():
    u.clear_console()
    new_player = Character(
        u.ask_str_input(f"Enter player {len(players) + 1}'s name: "),
        u.ask_int_input("Enter player's strength: "),
        u.ask_str_input("Enter player's weapon: ")
    )
    players.append(new_player)
    print(f"Character {new_player.name} created successfully")
    u.wait_for_enter()


def attack(attacker, action_type: Action):
    target = menus.select_player(
        players,
        f"{attacker.name}, choose the player to attack: "
    )
    if action_type == Action.PHYSICAL:
        if attacker.physical_attack(target):
            players.remove(target)
    elif action_type == Action.SPELL:
        if attacker.cast_spell(target, u.select_item(attacker.spells, "Select a spell: ")):
            players.remove(target)
    else:
        raise ValueError("Invalid action type")
    u.wait_for_enter()


def chat(character):
    character.chat(u.ask_str_input("Enter the message to say: "))
    u.wait_for_enter()


def handle_character_creation():
    nb_joueurs = u.ask_int_input("How many players? ")
    for i in range(nb_joueurs):
        create_player()


def play_turn(player):
    print(f"{player.name}'s turn")
    print(f"Remaining players: {', '.join([player.name for player in players])}")
    choice = menus.display_choices()
    if choice == 1:
        action = menus.select_action(player.name)
        if action == Action.PHYSICAL:
            attack(player, Action.PHYSICAL)
        elif action == Action.CHAT:
            chat(player)
        elif action == Action.SPELL:
            attack(player, Action.SPELL)
        return Status.CONTINUE
    elif choice == 2:
        return Status.STOP


def main():
    handle_character_creation()
    current_player = 0
    while len(players) > 1:
        u.clear_console()
        status = play_turn(players[current_player])
        if status is Status.STOP:
            print("Quitting game")
            return
        current_player += 1
        if current_player >= len(players):
            current_player = 0
    print(f"{players[0].name} won !")


main()
