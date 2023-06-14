#write a class calculator capable of finding square cube and squareroot of a no.
import math

class Calculator:
    def __init__(self,n):
        self.n=n
        print("square of",n,"is",n**2)
        print("cube of",n,"is",n**3)
        print("squareroot of",n,"is",math.sqrt(n))

cal1=Calculator(20)


