# server.py 
import socket                                                     #1                                                                                                 
import time                                                       #2
serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM) #3
host = socket.gethostname()                                       #4
port = 9999                                                      #5
serversocket.bind((host, port))                                   #6
serversocket.listen(5)                                            #7
while True:                                                       #8
	clientsocket,addr = serversocket.accept()                 #9
	print("Got a connection from %s" % str(addr))             #10
	currentTime = time.ctime(time.time()) + "\r\n"            #11
	clientsocket.send(currentTime.encode('ascii'))            #12
	clientsocket.close()                                      #13
