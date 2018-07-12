#!/usr/bin/python3

import socket
import sys

# Our server will listen on all interfaces, port 8888
host = ''
port = 8888

# Create a IP4v TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created.')

# Bind the socket to host:port
try:
    s.bind((host, port))
except socket.error:
    print('Binding failed.')
    sys.exit()
print('[{}] listening on port {}'.format(host, port))

# Establish number of clients that can connect to the socket
nclients = 10
s.listen(nclients)
print('Socket is ready for ' + str(nclients) + ' clients.')

# Accept a request from outside
conn, addr = s.accept() # returns a connection and the IP:port of the client
print('Connected with ' + addr[0] + ':' + str(addr[1]))

# Receive data from client if they send anything
while True:
    data = conn.recv(1024)
    print('Message received: ' + data.decode())
    if not data:
        break

# Close the connection and the socket
conn.close()
s.close()
