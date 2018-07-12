#!/usr/bin/python3

import socket
import sys
import _thread

# Our server will listen on all interfaces, port 8888
host = '0.0.0.0'
port = 8888

# Create a IP4v TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created.')

# Bind the socket to host:port
try:
    s.bind((host, port))
except socket.error as err:
    print(err)
    sys.exit()
print('[{}] listening on port {}...'.format(host, port))

# Start listening
s.listen()

def client_handler(conn, addr):
    # Handles client connections, listening for messages from them.
    # This will spin off its own thread.
    conn.send('\nWelcome to the server. Enter your message:\n'.encode())
    while True:
        data = conn.recv(1024)
        if data.decode() == '':
            print(addr[0] + ':' + str(addr[1]) + ' has been disconnected.')
            break
        reply = 'FROM [' + addr[0] + ':' + str(addr[1]) + ']: ' + data.decode()
        if not data:
            break
        print(reply)
    conn.close()

# Accept requests from clients
while True:
    conn, addr = s.accept() # returns a connection and the IP:port of the client
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    _thread.start_new_thread(client_handler, (conn, addr))

# Close the socket
s.close()
