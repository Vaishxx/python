# import turtle
# import math

# flower=turtle.Turtle()
# flower.color('red','yellow')

# flower.speed(10) #will speed up the arrow will 10x
# flower.begin_fill()
# for i in range(100):
#     flower.forward(math.sqrt(i)*10 )
#     flower.left(170)
# flower.end_fill()
# turtle.done()

import turtle
import math
flower=turtle.Turtle()
flower.color('red')

flower.speed(10) #will speed up the arrow will 10x

# for i in range(100):
#     flower.forward(math.sqrt(i)*10)
#     flower.left(i%90)

for i in range(2000):
    # flower.forward(math.sqrt(i)*2)
    flower.forward(10)
    flower.left(math.sin(i/10)*25)
    flower.left(20)

turtle.done()