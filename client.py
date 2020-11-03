# Client side code using TCP
import socket as sock

# Servers ip and port
ip = 'localhost'
port = 4200

# Create a socket for connecting to server
client = sock.socket(sock.AF_INET, sock.SOCK_STREAM, sock.IPPROTO_TCP)
# Connect to the server using servers ip and port
client.connect((ip, port))
# Send utf-8 encoded message to the server
client.send('Hello I am client'.encode("utf-8"))
# Recieve response from the erver
from_server = client.recv(1024)
# Decode and display message
print(f'Message from Server: {from_server.decode("utf-8")}')
# Close connection
client.close()
