import turtle
bob=turtle.Turtle()
# bob.forward(100) #will move the arrow forward till 100 pixels
# #in the above line the 100 represents the pixel amount

# bob.left(45)#will make an angle of 45 degree to the left
# bob.forward(100)#will move forward that 45 degree to hundred pixel
# bob.right(90)#90 degree to the right
# bob.forward(100)

#COLOR
                               #name of the site for the color shade-->https://www.colorspire.com/rgb-color-wheel/
#bob.color('green')            #will color the border as pink
bob.color('#FD8A07','pink')           #need to write '#' before the '#value'
#in the above line first color is border and second color is for fill color
#DRAWING A SQUARE
bob.begin_fill()
bob.forward(200)
bob.left(90)
bob.forward(200)
bob.left(90)
bob.forward(200)
bob.left(90)
bob.forward(200)
bob.end_fill()
turtle.done()