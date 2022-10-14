import utils as u
from models import Mentor, Bachelor
from enums import Status
from pve.engine import play_turn

# All variables and functions in this program are in French for consistency with the required attributes and methods
# from the "Personnage" class.

players = [
    Mentor("Robin", 25, "Gourd"),
    Bachelor("Lucas", 25, "Cringe"),
    Bachelor("Anthony", 25, "Poison"),
]


def create_player():
    u.clear_console()
    new_player = Bachelor(
        u.ask_str_input(f"Enter player {len(players) + 1}'s name: "),
        u.ask_int_input("Enter player's strength: "),
        u.ask_str_input("Enter player's weapon: ")
    )
    players.append(new_player)
    print(f"Character {new_player.name} created successfully")
    u.wait_for_enter()


def handle_character_creation():
    nb_joueurs = u.ask_int_input("How many players? ")
    for i in range(nb_joueurs):
        create_player()


def __main__():
    handle_character_creation()
    current_player = 0
    while len(players) > 1:
        u.clear_console()
        status, player_killed = play_turn(players[current_player])
        if status is Status.STOP:
            print("Quitting game")
            return
        current_player += 0 if player_killed else 1
        if current_player >= len(players):
            current_player = 0
    print(f"{players[0].name} won !")


__main__()
