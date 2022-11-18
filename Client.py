# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:36:38 2022

@author: wur5
"""
import socket
HOST = socket.gethostname()
PORT = 1234


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
running = False
server_sending = True
print("Connected to server.")


while not running:
    client_message = input("Client: ")
    s.send(client_message.encode("utf-8"))
    client_message = input("Client: ")
    s.send(client_message.encode("utf-8"))

    while server_sending:
        server_message = s.recv(1024)
        server_message = server_message.decode("utf-8")
        if server_message == "end":
            server_sending = False
        else:
            print(server_message)
        
    
    client_message = input("Client: ")
    s.send(client_message.encode("utf-8"))
    
    
s.close()