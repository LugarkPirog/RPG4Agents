import numpy as np
import json
import os
import sys
import logging
import socket
import time

if __name__ == '__main__':
    base_path = '.'
    sys.path.insert(0, os.path.abspath('.'))
else:
    base_path = '..'

from settings import DEBUG
from items.items import Empty, BaseItem
from world.world import PORT as WORLD_PORT


HOST = '127.0.0.1'
PORT = 322

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)


CLASSES = os.path.abspath(base_path) + '\\player\\classes.json'
print(os.path.exists(CLASSES))


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


class Player(object):
    """
    can move udrl, fight with autoattack (weapon) and skills
    """
    def __init__(self, name, player_class, position):
        self._class = player_class
        self.name = name

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

        self.s = socket.socket()
        self.s.connect((HOST, PORT))

    def notify(func):
        def f(self, *args, **kwargs):
            res = func(self, *args, **kwargs)
            msg = self.name + ' ' + func.__name__
            self.s.sendall(msg.encode('utf-8'))
            logging.debug('sending ' + msg)
            return res
        return f

    @notify
    def attack(self):
        return 1 + (self.wear['weapon']['damage'] or 0)*(self.stats['str']/5)

    @notify
    def cast(self, spell):
        pass

    def put_on(self, item):
        self.wear[item['type']] = item

    @notify
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
        return self.pos

    @notify
    def quit(self):
        pass

    def __str__(self):
        tmp = '{:9s}: {:15s}\n'
        s = ''
        s += tmp.format('Class', self._class)
        s += tmp.format('Name', str(self.name))
        s += tmp.format('Stats', str(self.stats))
        s += tmp.format('Pos', str(self.pos))
        return s


class PlayerFactory(object):
    @staticmethod
    def new_player(name, cls, pos):
        return globals()['Player'](name, cls, pos)


if __name__ == '__main__':
    import sys

    pname = sys.argv[1]

    p = Player(pname, 'warrior', [0, 0])
    it = BaseItem(id='2')
    p.put_on(it)

    # item wearing
    print(p.wear['weapon'])
    print(p.attack())

    # moving
    print(p.pos)
    for i in range(10):
        d = np.random.choice(['n', 's', 'w', 'e'])
        p.move(d)
        time.sleep(1)

    print(p.pos)
    p.quit()

    # level up

    # spell casting
