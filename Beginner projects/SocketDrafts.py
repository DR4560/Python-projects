import socket
socket.setdefaulttimeout(3)
newSocket = socket.socket()
newSocket.connect (("localhost", 22))

string.count('x'):
string.find('x'):
string.lower():
string.upper():
string.replace('a', 'b'):




#example

#!usr/bin/python


#Strings
a= "Python"
b = "Python\n"
c = "Python "
print (len(a))
print (len(b))
print (len(c))

#Lists

list1 = [1,2,3,4,5,6,7,9]
print(list1[2:4])

for x in list1:
    print(x)
list1.append(10)
a = list1.count(6)
for x in list1:
    print(x)

    print(a)

    dict = {'a1':5, 'a2':6}
    print(dict['a1'])

    a2 = {'apples':1, 'mango':2, 'orange':3}
    b2 = {'L':22, 'K':33, 'X':11}
    a2.update(b2)
    print(a2)

    del a2 ['mango']
    print(a2)

    import socket

    socket.setdefaulttimeout(3)
    newSocket = socket.socket()
    newSocket.connect(("localhost", 22))
    response = newSocket.recv(1024)
    print(response)



try:
    answer = 10/0
except ZeroDivisionError, e:
    answer = e
print (answer)


import socket #imported socket module
import sys

try:
    TCP_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print 'Error occurred while creating socket.Error code: ' + str(e[0]) +
' , Error message : ' + e[1]
    sys.exit();
print 'Success!'









import socket #Imported sockets module
import sys
TCP_IP = '127.0.0.1'
TCP_PORT = 8090 #Reserve a port
BUFFER_SIZE = 1024
MESSAGE_TO_SERVER = "Hello, World!"
try:
#Create an AF_INET (IPv4), STREAM socket (TCP)
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
print 'Error occurred while creating socket. Error code: ' + str(e[0])
+ ' , Error message : ' + e[1]
sys.exit();
tcp_socket.connect((TCP_IP, TCP_PORT))
try :
#Sending message
tcp_socket.send(MESSAGE_TO_SERVER)
except socket.error, e:
print 'Error occurred while sending data to server. Error code: ' +
str(e[0]) + ' , Error message : ' + e[1]
sys.exit()
print 'Message to the server send successfully'






#RECEIVING DATA


""" SAVE THIS DATA AS A SERVER.PY"""


import socket #Imported sockets module
from zipfile import sizeEndCentDir

from pymysql import connect

TCP_IP = '127.0.0.1'
TCP_PORT = 8090
BUFFER_SIZE = 1024
use small size
try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
    print
    'Error occurred while creating socket. Error code: ' + str(e[0]) +
    ' , Error message : ' + e[1]
    sys.exit();

tcp_socket.bind((TCP_IP, TCP_PORT))
tcp_socket.listen(2)
print ('Listening...')


#WAIT FOR BLOCKING CALL

connection, address = tcp_socket.accept()
print 'Connected with', address



data= connection.recv(BUFFER_SIZE)
print "Message from client:", data
connection.sendall("Connected successfully")
from client
connection.close()



#IMPORTANT TO KEEP SERVER ALIVE

while True:
    connection, address = tcp_socket.accept()
    print 'Client connected:', address

    data = connection.recv(BUFFER_SIZE)
    print "Message from client:", data
    connection.sendall("thanks for connection")











"""CLIENT.PY"""

import socket
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = 8090
BUFFER_SIZE =1024
MESSAGE_TO_SERVER = "Hello, world!"

try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error(e):
    print ('Error occured while creating socket.Error Error code: ' + str(e[0]) +' , Error message : ' + e[1]')
    sys.exit();

tcp_socket.connect((TCP_IP, TCP_PORT))

try:
    tcp_socket.send(MESSAGE_TO_SERVER)
    except socket.error, e:
    print 'Error occurred while sending data to server. Error code: ' +
    str(e[0]) + ' , Error message : ' + e[1]
    sys.exit()
    print 'Message to the server send successfully'
    data = tcp_socket.recv(BUFFER_SIZE)
    tcp_socket.close() #Close the socket when done
    print "Response from server:", data











"""HANDLING MULTIPLE CONNECTIONS"""

import socket
import sys

from numpy.lib.format import BUFFER_SIZE
from thread import *

TCP_IP = '127.0.0.1'
TCP_PORT = 8090 #reserving a port

try:
    # create an AF_INET (IPv4), STREAM socket (TCP)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
    print
    'Error occured while creating socket. Error code: ' + str(e[0]) +
    ' , Error message : ' + e[1]
    sys.exit();
    # Bind socket to host and port
    tcp_socket.bind((TCP_IP, TCP_PORT))
    tcp_socket.listen(10)
    print
    'Listening..'

def ClientConnectionHandler(connection):
    BUFFER_SIZE = 1024
    #sending msg to the client
    connection.send('Welcome here to my server')
    #infinite loop to keep the thread alive.
    while True:
        #receiving data from client
        data = connection.recv(BUFFER_SIZE)
        reply = 'Data received:'  + data
        if not data:
            break
        connection.sendall(reply)

    #Exiting loop
    connection.close()
#keep server alive always(infinite loop)
while True:
    connection, address = tcp_socket.accept()
    print 'Client connected:', address
    start_new_thread(ClientConnectionHandler, (connection,))
tcp_socket.close()










#now is about the
"""SOCKET SERVER"""
from turtledemo.clock import setup

#BaseServer(defines the API)
#TCPServer(uses TCP/IP sockets)
#UDPServer(uses Datagram sockets)
#UnixStreamServer(Unix-domain stream sockets)
#UnixDatagramServer(unix-domain datagram sockets)



setup()- prepare the request, handle() - parses the incoming requests,
finish() - clean up anything created during setup()


"""SIMPLE SERVER WITH THE SocketServer module"""

import SocketServer
class TCPRequesHandler(SocketServer.StreamRequesthandler ):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        self.request.sendall(self.data)

#create the server









import SocketServer

class TCPRequestHandler
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print "{} wrote: ".format(self.client_address[0])
        print self.data
        self.request.sendall(self.data)

server = SocketServer.TCPServer(("", 8090), TCPRequesthandler)
server.serve_forever







