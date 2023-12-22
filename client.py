import socket
import sys
import threading
#Импорт библиотек
    
    #HEADER - const значение, ЗАГОЛОВОК
HEADER_LENGTH = 10
HOST_IP = input('Please, type IP of server')
HOST = HOST_IP,10000

def send_msg(s):
    while True:
        print('Please, write a message')
        msg = input().encode('UTF-8')
        if msg: #если на вход поступило сообщение, то кодируем его и отправляем
            msg_header = f"{len(msg):<{HEADER_LENGTH}}".encode('UTF-8')
            s.send(msg_header+msg)
            print(msg_header, msg)

def recv_msg(s):
        while True:
            try: #Если нам поступает сообщение, содержащее заголовок, то принимаем его, показываем само сообщение и username того, кто отправил
                user_header =s.recv(HEADER_LENGTH)
                if not len(user_header):
                    sys.exit()
                user_lenght = int(user_header.decode('UTF-8').strip())
                username = s.recv(user_lenght)

                msg_header = s.recv(HEADER_LENGTH)
                msg_length = int(msg_header.decode('UTF-8').strip())

                data = s.recv(msg_length).decode('UTF-8')
                print(f"New message from {username.decode('UTF-8')} - {data}")
            except IOError as _ex:  
                pass



def main():

    username = input("Please type a username: ").encode('UTF-8')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(HOST)
    s.setblocking(False)

    header = f"{len(username):<{HEADER_LENGTH}}".encode('UTF-8')
    s.send(header + username)

    send_thread = threading.Thread(target=send_msg, args=(s,))
    recv_thread = threading.Thread(target=recv_msg, args=(s,))

    send_thread.start()
    recv_thread.start()

    send_thread.join()
    recv_thread.join()

if __name__ == "__main__":
    main()