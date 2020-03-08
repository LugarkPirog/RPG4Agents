"""
Give a try to event-based system
"""

import zmq
import time
import socket
import argparse

p = argparse.ArgumentParser()
p.add_argument('--ip', type=str, help='ip address to connect', default='127.0.0.1', dest='ip')
p.add_argument('-d', type=int, help='delay between sending', default='1', dest='delay')
args = p.parse_args()


cont = zmq.Context()
s = cont.socket(zmq.PUB)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#s.setblocking(False)

addr = 'tcp://' + args.ip + ':322'

s.bind(addr)
i = 0
n = args.delay
while True:
    msg = 'abc_' + str(n)
    s.sendall(msg.encode('utf-8'))
    time.sleep(n)
    print(str(i) + '\r', end='')
    i += 1

# python PycharmProjects/RPG4Agents/world/server.py