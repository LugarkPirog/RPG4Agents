import numpy as np


class WorldGrid:
    def __init__(self, field_size=5):
        self.players = []
        self.field_size = field_size
        self.grid = np.zeros((field_size, field_size))

    def create_player(self):
        pass

    def start(self):
        pass

