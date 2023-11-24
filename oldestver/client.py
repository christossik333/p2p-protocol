#!/usr/bin/env python3
import socket
import sys
from threading import Thread


def recv_m():
    while True:
            recv_data = newSocket.recv(1024)
            recv_msg = recv_data.decode('utf-8')
            if 'quit' in recv_msg or 'exit' in recv_msg or 'bye' in recv_msg:
                print('Host want to close the connection')
                newSocket.close()
                break
            print ('Server>', recv_msg)
            break


def send_msg():
    while True:
            msg = input(username+'>')
            if 'quit' or 'exit' or 'bye' in msg:
                print('Server has been closed')
                newSocket.close()
                break
            newSocket.send(msg.encode('utf-8'))
            break
    
newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket
sock_ip = input('Please input the server IP')#user types the server IP which recieve from owner of server
sock_port = 9490
username = input('Please input your username')
newSocket.connect((sock_ip , sock_port))


thread_recv = Thread (target = recv_m)
thread_send = Thread (target = send_msg)

thread_recv.start()
thread_send.start()

thread_send.join()
thread_recv.join()

newSocket.close()



