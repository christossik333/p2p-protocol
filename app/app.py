from flask import Flask, render_template, request, redirect, jsonify,redirect
import socket
import threading

# Импорт модулей

app = Flask(__name__, template_folder='templates') # папка с шаблонами /// still relative to module 

HEADER_LENGTH = 10 # Длина заголовка сообщения
s = None # Переменная для сокета
connected = False # Флаг состояния подключения
messages = [] # Список сообщений

def recv_msg(): # Если нам поступает сообщение, содержащее заголовок, то принимаем его, показываем само сообщение и username того, кто отправил
    global s, connected
    while True:
        try:
            user_header = s.recv(HEADER_LENGTH) # Получение заголовка сообщения (длина имени пользователя)
            if not len(user_header):
                break

            user_length = int(user_header.decode('utf-8').strip()) # Размер имени пользователя
            username = s.recv(user_length) # Получение имени пользователя

           
            msg_header = s.recv(HEADER_LENGTH) # Получение заголовка сообщения
            msg_length = int(msg_header.decode('utf-8').strip()) # Размер сообщения

            data = s.recv(msg_length).decode('utf-8')# Получение и декодирование сообщения
            # Проверка по никнейму отправителя
            sender_username = username.decode('utf-8')
            if sender_username == request.form['username']:
               update_messages(f"You {data}")
            else:
                update_messages(f"{sender_username} - {data}")
        except IOError as _ex:
            pass


@app.route('/') # Маршрут главной страницы
def index():
    if connected:
        return render_template('chat.html') # Отображение шаблона чата, если подключение установлено
    else:
        return render_template('connect.html') # Отображение шаблона для подключения


@app.route('/connect', methods=['POST']) # Маршрут к странице подключения к серверу
def connect(): 
    global s, connected
    HOST_IP = request.form['host_ip']
    PORT = 10000
    username = request.form['username'].encode('utf-8')
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST_IP, PORT))
    s.setblocking(False)
    

    header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
    s.send(header + username)
    # Код подключения к серверу и настройки сокета
    recv_thread = threading.Thread(target=recv_msg)
    recv_thread.start()

    connected = True
    return redirect('/')# Перенаправление на главную страницу после подключения

@app.route('/send', methods=['POST'])# Маршрут для отправки сообщений
def send(): #Отправка сообщений на сервер
    global s
    message = request.form['message'].encode('utf-8')
    if message and s:
        msg_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        s.send(msg_header + message)
        # Отправка сообщения на сервер

        # Маркировка исходящих сообщений
        update_messages(f"You: {message.decode('utf-8')}")

    return '', 204 # Возврат пустого ответа


@app.route('/get_messages')# Маршрут для получения сообщений в формате JSON
def get_messages():
    global messages
    return jsonify({'messages': messages})


def update_messages(message):
    global messages
    messages.append(message)# Добавление сообщения в список


if __name__ == '__main__': #Запуск приложения на всех IP, на 5000 порте
    app.run(host='0.0.0.0', port=5000, debug=True)
