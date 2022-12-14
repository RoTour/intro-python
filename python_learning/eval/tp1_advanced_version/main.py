import pvp.menus as pvp_menus
import menus as all_menus
import utils as u
import pve.engine as pve_engine
from models import Action, Status, Mentor, Bachelor, GameFeature

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


def attack(attacker, action_type: Action):
    target = all_menus.select_player(
        players,
        f"{attacker.name}, choose the player to attack: "
    )
    action = None
    if action_type == Action.PHYSICAL:
        action = attacker.physical_attack
    if action_type == Action.SPELL:
        action = attacker.cast_spell

    while True:
        player_killed, attack_successful = action(target) if action_type == Action.PHYSICAL \
            else action(
            target,
            u.select_item(attacker.spells, f"(Mana points: {attacker.mana_points}) | Select a spell: ")
        )
        if attack_successful:
            break
        u.wait_for_enter()

    if player_killed:
        players.remove(target)

    u.wait_for_enter()
    return player_killed


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
    choice = all_menus.select_game_feature()
    if choice == GameFeature.PVP.name:
        action = pvp_menus.select_pvp_action(player)
        if action == Action.PHYSICAL:
            return Status.CONTINUE, attack(player, Action.PHYSICAL)
        elif action == Action.SPELL:
            return Status.CONTINUE, attack(player, Action.SPELL)
        elif action == Action.CHAT:
            chat(player)
            return Status.CONTINUE, False
    elif choice == GameFeature.PVE.name:
        pve_engine.start_random_fight(player)
        return Status.CONTINUE, False
    elif choice == GameFeature.QUIT.name:
        return Status.STOP, False
    return Status.CONTINUE, False


def main():
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


main()
