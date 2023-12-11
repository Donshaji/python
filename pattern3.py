#rotating square
import turtle
tr=turtle.Turtle()
xi=5
def draw_sq(xi):
    tr.up()
    tr.goto(-xi,-xi)
    tr.pendown()
    for i in range(4):
        tr.forward(xi*2)
        tr.left(90)
for i in range(50):
    draw_sq(xi)
    xi=xi+10
    tr.right(10)