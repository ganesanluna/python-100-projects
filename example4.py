#example4.py source code
import os,sys                               #1
def ls():                                   #2
    dir=input("enter your path : ")         #3
    filenames=os.listdir(dir)               #4
    for filename in filenames:              #5
        path=os.path.join(dir,filename)     #6
        print(os.path.abspath(path))        #7
if __name__ == '__main__':                  #8
    ls()                                    #9
        
