# example15.py Python program to swap two variable
x = int(input('Enter value of x: '))                        #1
y = int(input('Enter value of y: '))                        #2

temp = x                                                    #3
x = y                                                       #4
y = temp                                                    #5

print('The value of x after swapping: {}'.format(x))        #6
print('The value of y after swapping: {}'.format(y))        #7
