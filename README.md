# :space_invader: p2p-protocol || Nexus - simple P2P chat

```


 /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )
 > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 
 /\_/\     _   _ _______  ___   _ ____     /\_/\ 
( o.o )   | \ | | ____\ \/ / | | / ___|   ( o.o )
 > ^ <    |  \| |  _|  \  /| | | \___ \    > ^ < 
 /\_/\    | |\  | |___ /  \| |_| |___) |   /\_/\ 
( o.o )   |_| \_|_____/_/\_\\___/|____/   ( o.o )
 > ^ <                                     > ^ < 
 /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )
 > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 


```
![Изображение](https://iili.io/JAOPtRI.png "Логотип Nexus")

:godmode:  Nexus is a simple Peer-To-Peer chat with a graphical interface and written in Python using the socket module. This is a computer science project that we haven't completed, please don't beat it)

## **Peer-To-Peer** VS standart **Client-Server** model

 A regular **Client-Server** based chat:
```
            \<----\                /---->/  
Client A                Server                Client B 
            /---->/                \<----\
```

 A **Peer-To-Peer** based chat:
```
            /---->/  
Client A              Client B 
            \<----\
```

As we can see in the chat version using P2P, no third-party server is involved in the connection, and a user can simultaneously act as both a client and a server.
All messages come directly and are not forwarded to third parties.

## Quickstart
```
# Install dependencies
python -m pip install -r requirements.txt

# Install fonts
\p2p-protocol\app\static\fonts

# Start server in one terminal
py server.py

#Start client app in another terminal
py app/app.py

Thats all!
___enjoy this piece of bad code!___
```
There is also a version in Russian:
[rusREADME](https://github.com/christossik333/p2p-protocol/blob/main/rusREADME.md)

## :technologist: Members:

:shipit: [Гвоздев Илья] (https://github.com/Kvelmi)

:shipit: [Гончарова Кристина] (https://github.com/Kristina-lox)

:shipit: [Макерова Марта] (https://github.com/maura45773)

:shipit: [Никитина Кристина] (https://github.com/christossik333)