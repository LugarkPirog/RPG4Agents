import zmq
import argparse
import socket

p = argparse.ArgumentParser()
p.add_argument('--ip', type=str, help='ip address to connect', default='127.0.0.1', dest='ip')
args = p.parse_args()


c = zmq.Context()
s = c.socket(zmq.SUB)
addr = 'tcp://' + args.ip + ':322'
s.connect(addr)

s.setsockopt_string(zmq.SUBSCRIBE, '')
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#s.setblocking(False)

print('Connected')
i = 0

while True:
    print(str(i) + '\r', end='')
    st = s.recv(2048)
    print(st.decode('utf-8'))
    i += 1

# python PycharmProjects/RPG4Agents/world/client.py