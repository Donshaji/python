#program to draw simple 5 circle in the screen using python turtle
import turtle
tr=turtle.Turtle()
def draw_circle(x,y,color_f,r):
    tr.up()
    tr.goto(x,y)
    tr.down()
    tr.begin_fill()
    tr.fillcolor(color_f)
    tr.circle(r)
    tr.end_fill()
draw_circle(0,0,"green",50)
draw_circle(100,100,"orange",50)
draw_circle(-100,100,"blue",50)
draw_circle(-100,-100,"red",50)
draw_circle(100,-100,"yellow",50)