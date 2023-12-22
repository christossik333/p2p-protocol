#select — waiting for I/O completion

import socket
import select
import sys
# Импорт библиотек

#HEADER - const значение, ЗАГОЛОВОК
HEADER_LENGTH = 10 # Длина заголовка сообщения
sock_ip = '192.168.187.213', 10000 # IP-адрес и порт

# Создание серверного сокета и его настройка
   
#AF_INET - IP, SOCK_STREAM - TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(sock_ip)
server.listen()

# Вывод информации о начале работы сервера

print('Server was started\n',sock_ip)
print ('I am listening your connections') #создаём сервер и привязываем его к localhost с портом 10000

# Инициализация списков для отслеживания сокетов и клиентов

#sockets_list - информация о текущих сокетах, clients_list - информация о текущих клиентах
sockets_list = [server]
clients = {}

# Функция приема сообщений от клиента
def receive_msg(client: socket.socket):
    try:
        # Считывание длины сообщения (залоговка) для подготовки буфера
        msg_header = client.recv(HEADER_LENGTH) #msg_header = ЗАГОЛОВОК СООБЩЕНИЯ
        if not len(msg_header):
            return False    
        
        msg_length = int(msg_header.decode('UTF-8').strip())
        
        return {
            'header': msg_header, # Информация о заголовке
            'data': client.recv(msg_length), # Декодируемое сообщение
        }

    except:
        return False 



# Отслеживание входящих подключений и обработка сообщений
while True:
    rs, _, xs = select.select(sockets_list, [], sockets_list)
    for _socket in rs:
        if _socket == server:
            client_socket, addr = server.accept()

            user = receive_msg(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user

            print(f'New connection from {addr} with data {user["data"]}')

        else:
            msg = receive_msg(_socket)
            if msg is False:
                print(f'Connection from {clients[_socket]["data"]} has been interrupted')
                sockets_list.remove(_socket)
                del clients[_socket]
                continue

            user = clients[_socket]

            # Отправка сообщения каждому клиенту, кроме отправителя
            for client_socket in clients:
                if client_socket != _socket:
                    client_socket.send(user['data'] + msg['header'] + msg['data'])

    for _socket in xs:
        sockets_list.remove(_socket)
        del clients[_socket]