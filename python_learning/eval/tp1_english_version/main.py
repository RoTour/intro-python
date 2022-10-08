from models import Character, Action, Status
import utils as u
import menus

# All variables and functions in this program are in french for consistency with the required attributes and methods
# from the "Personnage" class.

players = []


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


def attack(attacker):
    target = menus.select_player(
        players,
        f"{attacker.name}, choosse the player to attack: "
    )
    is_killed = attacker.attack(target)
    if is_killed:
        players.remove(target)
    u.wait_for_enter()


def chat(character):
    character.chat(u.ask_str_input("Enter the message to say: "))
    u.wait_for_enter()


def handle_character_creation():
    nb_joueurs = u.ask_int_input("How many players? ")
    for i in range(nb_joueurs):
        create_player()


def play_turn(personnage):
    print(f"{personnage.name}'s turn")
    print(f"Remaining players: {', '.join([personnage.name for personnage in players])}")
    choice = menus.display_choices()
    if choice == 1:
        action = menus.select_action()
        if action == Action.ATTACK:
            attack(personnage)
        elif action == Action.CHAT:
            chat(personnage)
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
