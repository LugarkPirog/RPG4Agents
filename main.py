__doc__ = '''
The game:
2d field, players can move udlr, if 2 players on 1 cell - fight.
Character stats: str, dex, int, etc
Classes: different skills
Chests: At some cells, contain some loot
Equipment: players have some armor, weapon n other things
Item upgrading: to4ka, with some prob can add +1 to item tier, advancing its stats
Optional - leaderboards: LB for pvp, gear and mb other

'''
import os
import sys
from world.world import *


#def main(**kw):
#    pass

class B:
    def __init__(self):
        pass

    def __set__(self, instance, value):
        instance.x = value[0]
        instance.y = value[1]

    def __get__(self, instance, owner):
        return instance.x, instance.y


class A:
    b = B

    def __init__(self):
        self.x = 0
        self.y = 0


a = A()
a.b = 10, 10
print(a.b)

#if __name__ == '__main__':
    #w = WorldGrid()
    #w.start()

