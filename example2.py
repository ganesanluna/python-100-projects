#example2.py source code
import turtle           #1
t=turtle.Pen()          #2
turtle.bgcolor('green') #3
t.color('blue')         #4
t.begin_fill()          #5
for x in range(1,73):   #6
    t.forward(250)      #7
    t.right(185)        #8
t.end_fill()            #9
