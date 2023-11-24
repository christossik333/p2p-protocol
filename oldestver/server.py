#!/usr/bin/env python3
import socket
from threading import Thread

def recv_m():
    while True:
        recv_data = newSocket.recv(1024)
        recv_msg = recv_data.decode('utf-8')
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
        newSocket.send(msg.encode('utf-8'))


#def get_local_ip():
 #   hostname = socket.gethostname()
  #  local_ip = socket.gethostbyname(hostname)
   # return local_ip


port = 9490
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket

#ock_ip = socket.gethostbyname(socket.gethostname())
sock_ip = '127.0.0.1'

s.bind((sock_ip,port))
s.listen(3) #how much connections socket will be enter
print('Chat is running...',sock_ip,port)

newSocket, clientAddr = s.accept()
print('Connect with client {} successfully'.format(newSocket.getpeername()))

thread_recv = Thread (target = recv_m)
thread_send = Thread (target = send_msg)
thread_send.start()
thread_recv.start()
thread_send.join()
thread_recv.join()
newSocket.close()

s.close()