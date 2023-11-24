#!/usr/bin/env python3
import socket
from threading import Thread


def recv():
    while True:
        recv_data = newSocket.recv(1024)
        recv_msg = recv_data.decode()
        if recv_msg == 'quit' or 'exit' or 'bye':
            print('Host want to close the connection')
            newSocket.close()
            break
        print ('>', recv_msg)


def send_msg():
    while True:
        msg = input(username+'>')
        if 'quit' or 'exit' or 'bye' in msg:
            print('Server has been closed')
            newSocket.close()
            break
        newSocket.send(msg.encode())
    
newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket
#sock_ip = input('Please input the server IP')
#sock_port = input('Please input the server port')
sock_ip = '192.168.94.213' #my local IP
sock_port = 9490
username = input('Please input your username')
newSocket.connect((sock_ip , sock_port))


thread_recv = Thread (target = recv)
thread_send = Thread (target = send_msg)
thread_send.start()
thread_recv.start()
thread_send.join()
thread_recv.join()

newSocket.close()

newSocket.close()
