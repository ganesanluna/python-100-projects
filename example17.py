import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("red")
tess.penup()
size=15
for i in range(100):
    tess.stamp()
    size=size+1
    tess.forward(size)
    tess.right(24)
wn.mainloop()
