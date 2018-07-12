#!/usr/bin/python3

'''
This is the client. It makes a TCP (SOCK_STREAM) connection with IPv4 (AF_INET).
It gets the remote IP based on the host's name and makes a connection.
'''

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to connect.')
    sys.exit()

print('Socket Created.')

host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.error:
    'Could not resolve {}.'.format(host)
    sys.exit()

print('IP address: ' + remote_ip)

s.connect((remote_ip, port))

print('Socket connected to ' + host + ' using IP: ' + remote_ip)
