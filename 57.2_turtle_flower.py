import turtle
flower=turtle.Turtle()
flower.color('red','yellow')

flower.speed(10) #will speed up the arrow will 10x
flower.begin_fill()
for i in range(36):
    flower.forward(300)
    flower.left(170)
flower.end_fill()
turtle.done()