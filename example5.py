#example5.py open file source code
import sys                                                  #1
def write():                                                #2
    name = input('Enter open of text file: ')               #3
    try:                                                    #4
        file = open(name,'rb+')                             #5
        print(file.read())                                  #6
        file.close()                                        #7
    except:                                                 #8
        print('Something went wrong!ONLY txt FILE : ')      #9
        sys.exit(0) # quit Python                           #10
write()                                                     #11
