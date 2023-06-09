# Original Code and Tutorial by Nathan Jennings https://realpython.com/python-sockets/

import socket

HOST = "phils-pi.lan"
PORT = 63322

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                     break
                conn.sendall(data)