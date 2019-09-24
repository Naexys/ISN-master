import socket
import time
from intValues import *

Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Host = '192.168.0.27'
Port = 1111
x = 50
y = 100
Sock.connect((Host, Port))

if raspberry:
    msgx="start"
    Sock.send(msgx.encode())
    time.sleep(0.05)

