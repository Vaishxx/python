import turtle
ptr = turtle.Turtle()
ptr.color("black","red")
screen = turtle.Screen()
ptr.speed(4)
ptr.begin_fill()

while True:
    ptr.forward(200)
    ptr.left(170)
    if abs(ptr.pos()) < 1:
        break

ptr.end_fill()
screen.exitonclick()
