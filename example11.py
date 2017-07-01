#example11.py source code
_author="BaluGanesan"                               #1
import hashlib                                      #2
filename=input("enter you file location : ")        #3
hasher = hashlib.md5()                              #4
with open(filename,'rb') as afile:                  #5
    buf = afile.read()                              #6
    hasher.update(buf)                              #7
print(hasher.hexdigest())                           #8
