import numpy as np
import json
import os
import logging
from settings import DEBUG
from items.items import Empty, BaseItem

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)


CLASSES = os.path.abspath('..') + '\\player\\classes.json'


def add_new_class(name, strength, dexterity, intellegence, vitality):
    data = {name:
                {'str': strength,
                 'dex': dexterity,
                 'int': intellegence,
                 'vit': vitality
                 }
            }

    with open(CLASSES, 'r') as f:
        d = json.load(f)
        f.close()
    d.update(data)

    with open(CLASSES, 'w') as f:
        json.dump(d, f)
        f.close()


class Player:
    """
    can move udrl, fight with autoattack (weapon) and skills
    """
    def __init__(self, player_class, position):
        self._class = player_class

        def load_stats():
            with open(CLASSES, 'r') as f:
                stats = json.load(f)[player_class]
                f.close()
            return stats

        self.stats = load_stats()
        self.wear = {k: Empty() for k in ['head', 'chest', 'arms', 'legs', 'weapon']}
        self.level = 0
        self.experience = 0
        self.health = self.stats['vit']*3 + 5

        self.pos = position

    def attack(self):
        return 1 + (self.wear['weapon']['damage'] or 0)*(self.stats['str']/5)

    def cast(self, spell):
        pass

    def put_on(self, item):
        self.wear[item['type']] = item

    def move(self, direction):
        if direction == 'n':
            self.pos[0] +=1
        elif direction == 's':
            self.pos[0] -= 1
        elif direction == 'w':
            self.pos[1] -= 1
        elif direction == 'e':
            self.pos[1] += 1
        else:
            pass


if __name__ == '__main__':
    p = Player('warrior', [0, 0])
    it = BaseItem(id='1')
    p.put_on(it)

    # item wearing
    print(p.wear['weapon'])
    print(p.attack())

    # moving
    print(p.pos)
    p.move('n')
    p.move('w')
    p.move('w')
    print(p.pos)

    # level up

    # spell casting
