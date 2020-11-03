# TCP-server-client-applicaiton-in-python
A simple server client application using TCP in python.

## Overview  
In the server client model, the server provides resources to the  clients. The server listens for connections on a particular host  whereas the clients send requests to the server.  
## The Server-side
On the Server side we bind the create a socket and bind it with  an ip and address on the server machine and listen and wait for  connections from the client. In the simple application the  server will display the message sent by client on the console  and respond it with a message saying ‘Hello I am server’.  
## The Client-Side
The client connects to the server socket on the address of the  server and sends it a message saying ‘Hello I am client’ and  displays the response from the server on the console. 

