#!/usr/bin/python           # This is client.py file
'''
follow: http://www.tutorialspoint.com/python/python_networking.htm
'''
import socket  # Import socket module

#create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'google.com'  # Get local machine name
port = 80  # Reserve a port for your service.

s.connect((host, port))
s.send('GET / HTTP/1.1 \n\n\n')
data = None
while 1:
    data = s.recv(1024)
    if not data:
        break
    print data 
s.close  # Close the socket when done
