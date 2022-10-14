import random

import utils as u
from fights.actions import select_fight_action
from menus import select_game_feature
from models import Character
from pve.enemies import Skeleton, Orc, IEnemy
from enums import Status, Action, GameFeature


def start_fight(players, bots):
    entities = players + bots
    random.shuffle(entities)

    current_entity = 0
    while len(entities) > 0 and len(bots) > 0:
        u.clear_console()
        print(f"curent entity: {entities[current_entity].name}")
        print("-----------------")
        print(f"Remaining fighters: {', '.join([self.name for self in entities])}")
        print("-----------------")
        print(f"{entities[current_entity].name}'s turn")

        if issubclass(type(entities[current_entity]), IEnemy):  # Enemy turn
            target_killed, _ = entities[current_entity].attack(random.choice(players))
        else:  # Player turn
            status, target_killed = fight_turn(entities[current_entity], bots)
            if status is Status.STOP:
                print("Quitting game")
                return
        current_entity += 0 if target_killed else 1
        print(f"target_killed: {target_killed}, current_entity: {current_entity}")
        u.wait_for_enter()
        if current_entity >= len(entities):
            current_entity = 0


def start_random_fight(player):
    enemies = []
    created_enemies = {Skeleton: 0, Orc: 0}
    for i in range(random.randint(1, 3)):
        enemy = random.randint(0, 10)
        if enemy < 10:
            created_enemies[Skeleton] += 1
            enemies.append(Skeleton(str(created_enemies[Skeleton])))
        else:
            created_enemies[Orc] += 1
            enemies.append(Orc(str(created_enemies[Orc])))
    start_fight([player], enemies)


def play_turn(character):
    print(f"{character.name}'s turn")
    print(f"Remaining players: {', '.join([self.name for self in Character.instances])}")
    choice = select_game_feature()
    if choice == GameFeature.PVP.name:
        return fight_turn(character)
    elif choice == GameFeature.PVE.name:
        start_random_fight(character)
        return Status.CONTINUE, False
    elif choice == GameFeature.QUIT.name:
        return Status.STOP, False
    return Status.CONTINUE, False


def fight_turn(character, targets):
    action = select_fight_action(character)
    if action == Action.PHYSICAL:
        return Status.CONTINUE, character.attack(Action.PHYSICAL, targets)
    elif action == Action.SPELL:
        return Status.CONTINUE, character.attack(Action.SPELL, targets)
    elif action == Action.CHAT:
        character.chat()
        return Status.CONTINUE, False
    return Status.CONTINUE, False
