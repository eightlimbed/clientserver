#!/usr/bin/python3

import socket
import sys

# Attempt to create a IPv4 (AF_INET) / TCP (SOCK_STREAM) socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to connect.')
    sys.exit()
print('Socket Created.')

# Get the host's IP address
host, port = 'www.google.com', 80
try:
    remote_ip = socket.gethostbyname(host)
except socket.error:
    'Could not resolve {}.'.format(host)
    sys.exit()
print('IP address: ' + remote_ip)

# Connect to the remote IP
s.connect((remote_ip, port))
print('Socket connected to ' + host + ' using IP: ' + remote_ip)

# Send a message to the host
message = 'GET / HTTP/1.1\r\n\r\n'
try:
    s.sendall(message.encode())
except socket.error:
    print('Did not send successfully.')
    sys.exit()
print('Message sent successfully.'.format(message))

# Get the response back
reply = s.recv(4096)
print(reply.decode())

# Close the socket
s.close()
