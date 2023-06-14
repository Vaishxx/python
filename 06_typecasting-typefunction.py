#string to integer conversion
a="3445" #this is a string data type
print(type(a))

a=int(a)  #this is type casting
# type casting is used to change the data type of variable if possible
print(a+2)

b="45ads"
#b gives error if typecasting is done because it cant be possible to change this string into integer


#integer to string  conversion
c=31  #here "31" is a string literal and 31 is a numeric literal
print(type(c))
c=str(c)
print(c)
print(type(c))