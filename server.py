#!/usr/bin/env python3
import socket
from threading import Thread

def recv():
    while True:
        recv_data = newSocket.recv(1024)
        recv_msg = recv_data.decode()
        if recv_msg == 'quit' or 'exit' or 'bye':
            print('Server has been closed')
            newSocket.close()
            break
        print ('Client>', recv_msg)

def send_msg():
    while True:
        msg = input('Server>')
        if 'quit' or 'exit' or 'bye' in msg: # this part of code doesnt work
            print('Server has been closed')
            newSocket.close()
            break
        newSocket.send(msg.encode())





s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket
s.bind(('192.168.94.213',9490)) # connect socket with port, where he will be waiting for connection #192.168.94.213 is my local ip
s.listen(20) #how much connections socket will be enter
print('Chat is running...{}'.format(s.getsockname()))

newSocket, clientAddr = s.accept()
print('Connect with client {} successfully'.format(newSocket.getpeername()))

thread_recv = Thread (target = recv)
thread_send = Thread (target = send_msg)
thread_send.start()
thread_recv.start()
thread_send.join()
thread_recv.join()

newSocket.close()

s.close()






