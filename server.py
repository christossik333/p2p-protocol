#select — waiting for I/O completion

import socket
import select
import sys

#HEADER - const значение, ЗАГОЛОВОК
HEADER_LENGTH = 10
HOST = ('localhost',10000)

#AF_INET - IP, SOCK_STREAM - TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(HOST)
server.listen()
print ('I am listening your connections')

#sockets_list - информация о текущих сокетах, clients_list - информация о текущих клиентах
sockets_list = [server]
clients_list = {}

#принятие входящих сообщений от клиента
def receive_msg(client: socket.socket):
    try:
        #считывание длины сообщения (залоговка) для подготовки буфера
        msg_header = client.recv(HEADER_LENGTH) #msg_header = ЗАГОЛОВОК СООБЩЕНИЯ
        if not len(msg_header):
            return False    
        
        msg_length = int(msg_header.decode('UTF-8').strip())
        
        return {
            'header': msg_header, #информация о заголовке
            'data': client.recv(msg_length), #декодируемое сообщение
        }

    except:
        return False 


#Отслеживание входящих подключений
while True:
    rs, _, xs = select.select(sockets_list, [] , sockets_list) #сокеты, готовые к чтению/отправке сообщений. 
    #rs - готовые к отправке, _ - готовые к чтению, xs - диагностика
    for _socket in rs:
        if _socket == server:
            client, addr = server.accept()

            user = receive_msg(client)
            if user is False:
                continue
            sockets_list.append(client)
            clients_list[client] = user

            print(f'New connection from {addr} with data {user["data"]}')

        else:
            msg = receive_msg(client)
            if msg is False: #Если нет сообщения, если в нём нет заголовка, то мы разрываем соединение с пользователем, удаляем его из списка рабочих сокетов и из списка пользователей
                print (f'Connection from {addr} has been interrupted')
                sockets_list.remove(_socket)
                del clients_list[_socket]
                continue
            
            user = clients_list[_socket]


            for client in clients_list: #рассылка сообщений
                if client is not _socket:
                    client.send(user["header"]+user["data"]+msg["header"]+msg["data"])

        for _socket in xs: #если в сокете ошибка - удаляем
            sockets_list.remove(_socket)
            del clients_list[_socket]

