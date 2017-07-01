# client.py 
import socket # create a socket object                          #1       
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           #2
host = socket.gethostname()                                     #3
port = 9999 # connection to hostname on the port.               #4
s.connect((host, port)) # Receive no more than 1024 bytes       #5    
tm = s.recv(1024)                                               #6
s.close()                                                       #7
print("The time got from the server is %s" % tm.decode('ascii'))#8
