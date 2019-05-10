import numpy as np
import socket
import _thread

HOST = '127.0.0.1'
PORT = 322


class WorldGrid(object):
    def __init__(self, field_size=5):
        self.field_size = field_size
        self.grid = np.zeros((field_size, field_size))
        self.starting_pos = [0, 0]
        self.players = {}

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

        self.s.bind((HOST, PORT))
        self.s.listen()
        print('Started. Listening')

    @staticmethod
    def threaded_conn(conn, addr=None):
        while True:
            msg = conn.recv(2048)
            if msg:
                try:
                    usr, act, data = msg.decode().split(';')
                    print(usr, act, data, '\r', end='')
                except ValueError:
                    print('Corrupted data :(', msg.decode())
            else:
                print('Stopped.')
                break
            if act == 'quit':
                print('\nPlayer', usr, 'disconnected!')
                break
        conn.close()

    def get_all_players_positions(self):
        positions = {a.name: a.pos for a in self.players}
        return positions

    def start(self, show=True):
        while True:
            conn, addr = self.s.accept()
            print('Connected!')
            _thread.start_new_thread(self.threaded_conn, (conn, addr))


if __name__ == '__main__':
    import sys

    mode = sys.argv[1]

    if mode == 'server':
        w = WorldGrid()
        w.start()

# python PycharmProjects/RPG4Agents/world/world.py server
