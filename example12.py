#example12.py source code
_author="ganesan"       
import os                                                                         #1
from subprocess import call                                                       #2                                                                                             
while True:                                                                       #3
	message = raw_input("1)ipconfig\n2)ping google\n3)arp -a\n")              #4
	if message == '1' :                                                       #5
		call(["ipconfig"])                                                #6
	elif message == '2' :                                                     #7
		call(["ping","google.com"])                                       #8
	elif message == '3' :                                                     #9
		call(["arp","-a"])                                                #10
	else :                                                                    #11
		break                                                             #12
