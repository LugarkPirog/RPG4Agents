import numpy as np
import zmq

PORT = '322'


class WorldGrid(object):
    def __init__(self, field_size=5):
        self.field_size = field_size
        self.grid = np.zeros((field_size, field_size))
        self.starting_pos = [0, 0]
        self.players = []

        c = zmq.Context()
        self.s = c.socket(zmq.SUB)
        self.s.connect('tcp://localhost:322')
        self.s.setsockopt_string(zmq.SUBSCRIBE, '')
        print('Connected')

    def get_all_players_positions(self):
        positions = {a.name: a.pos for a in self.players}
        return positions

    def start(self, show=True):
        while True:
            print('Waiting for data')
            msg = self.s.recv()
            print(msg)


if __name__ == '__main__':
    import sys

    mode = sys.argv[1]

    if mode == 'server':
        w = WorldGrid()
        w.start()

# python PycharmProjects/RPG4Agents/world/world.py server
