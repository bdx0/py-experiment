#!/usr/bin/python           # This is client.py file
'''
follow: http://www.tutorialspoint.com/python/python_networking.htm
'''
import socket  # Import socket module

s = socket.socket()  # Create a socket object
host = 'google.com'  # Get local machine name
port = 80  # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close  # Close the socket when done
