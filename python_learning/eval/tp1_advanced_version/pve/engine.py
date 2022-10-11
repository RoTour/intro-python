import random

import utils
from pve.enemies import Skeleton, Orc, IEnemy


def start_fight(players, bots):
    entities = players + bots
    random.shuffle(entities)
    for entity in entities:
        print(issubclass(type(entity), IEnemy), entity.__class__.__name__, entity.name)
    utils.wait_for_enter()

    # while len(players) > 0 and len(bots) > 0:
    #     for player in players:
    #         if len(bots) == 0:
    #             break
    #         # TODO: select action
    #     for player in bots:
    #         if len(players) == 0:
    #             break
    #         # TODO: select action


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
