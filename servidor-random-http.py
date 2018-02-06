#!/usr/bin/python3

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)
try:
    while True:
        number = random.randint(1, 1000000)
        link = "http://localhost:1234/" + str(number)
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP request received:')
        print(recvSocket.recv(2048))
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
        bytes ('<a href=' + link + '>Dame otra</a>\r\n', 'utf-8') +
        b"<html><body><h1>Hello World!</h1></body></html>" +
        b"\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
