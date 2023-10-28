# p2p-protocol
"Program Name" is a encrypted **peer-to-peer** messaging platform written in Python.

## **Peer-To-Peer** VS standart **Client-Server** model

# A regular **Client-Server** based chat:

            \<----\                /---->/  
Client A                Server                Client B 
            /---->/                \<----\


# A **Peer-To-Peer** based chat:


            /---->/  
Client A              Client B 
            \<----\


As we can see in the chat version using P2P, no third-party server is involved in the connection, and a user can simultaneously act as both a client and a server.
All messages come directly and are not forwarded to third parties.