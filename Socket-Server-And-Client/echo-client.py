# Source Code and Tutorial by Nathan Jennings https://realpython.com/python-sockets/

import socket

HOST = "phils-pi.lan"
PORT = 63322

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")