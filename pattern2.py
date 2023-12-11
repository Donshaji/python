#create golden ratio pattern
import turtle
tr=turtle.Turtle()
size=0
i=0
while i<100 :
    size=size+5
    tr.circle(size,steps=4)
    tr.left(5)
    i=i+1
    