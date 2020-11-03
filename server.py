# Server side code using TCP
import socket as sock

# IP and port for server
ip = 'localhost'
port = 4200

# Create a server socket for listening
server = sock.socket(
    sock.AF_INET,  # Address Family ipv4
    sock.SOCK_STREAM,  # It is a TCP socket
    sock.IPPROTO_TCP  # It will use TCP protocol
)

# binding socket to the ip and port
server.bind((ip, port))
# Start listening for connections from clients
server.listen(5)
print('Server Up ...')

while True:
    print('Waiting for Connections ...')
    # Accept an incoming connection
    conn, addr = server.accept()
    # Empty string to concatenate incoming string data
    from_clinet = ''
    while True:
        # Recieve data from client
        data = conn.recv(1024)
        if not data:
            break
        # decode it to string from utf-8
        from_clinet += data.decode("utf-8")
        print(from_clinet)
        # Send a utf-8 encoded Message to the cleint using client connection
        conn.send('Hello I am server'.encode("utf-8"))
    # Close the connection when data is recieved
    conn.close()
    print('client disconnected')
