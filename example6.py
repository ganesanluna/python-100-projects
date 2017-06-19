#example6.py write ource code
import sys       `                                       #1
def write():                                             #2
    name = raw_input('Enter name of text file: ')        #3
    try:                                                 #4
        file = open(name,'wb+')                          #5
        x=raw_input("enter your text : ")                #6
        file.write(x)                                    #7
        file.close()                                     #8
    except:                                              #9
        print('Something went wrong! Can\'t tell what?') #10
        sys.exit(0)                                      #11
write()                                                  #12
