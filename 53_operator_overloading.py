'''
operator overloading in python can be overloaded using dudnder methods.
These methods are called when the given operator is used on the object.
operators in the python can be overloaded using the following methods'''
class Number:
    def __init__(self,n):
        self.n=n
    def __add__(self,num2):
        return self.n+ num2.n

n1=Number(4)
n2=Number(6)
sum=n1+n2
print(sum)

#similarly __mul__ is used for multiplication
'''
p1+p2----> p1__add__(p2)
p1-p2---->p1__sub__(p2)
p1*p2---->p1__mul__(p2)
p1/p2---->p1__truediv__(p2)
p1//p2--->p1__floordiv__(p2)'''