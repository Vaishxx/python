import turtle
stars=turtle.Turtle()
stars.getscreen().bgcolor("#994444")
stars.penup()
stars.goto((-200,100))
stars.pendown()

def shape(turtle,size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            shape(turtle,size/3)
            turtle.left(216)
        turtle.end_fill()    
shape(stars,360)
turtle.done()