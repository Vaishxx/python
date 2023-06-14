def avg(marks):    #function named avg(marks)
    p=((marks[0]+marks[1]+marks[2]+marks[3])/4)

    return p
marks1=[12,34,56,78]
avg1=avg(marks1)

marks2=[11,4,96,68]
avg2=avg(marks2)
print(avg1,avg2)

#A function is a group of statement performing a specific task.
#When a program gets bigger in size and its complexity grows,it gets difficult for a programmer to keep track on which piece of code is doing what.
# A function can be reused by a programmer in a given program og any no. of times

#syntax:
# def func1():
#     print("hello")  ----> this is called function definition
# this function can be called any no. of time anywhere in the program
# FUNCTION CALL- Whenever we need to call a function we put the name of the function followed by paranthesis as follows:
#          funct1()  --->this is called function calling 
#FUNCTION DEFINITION- The part containing the exact set of intruction which are executed during the function call

# wap to greet a user with "good day" using functions
def greet(name):
    print("good day "+name)
greet("Vaishnavi") 

#There are 2 types of functions:-
#Built in function-already persent in python eg-sum,range,print,len() etc
#User defined function- defined by users

#FUNCTION WITH ARGUMENTS-A function can accept some values it can work with.We can put these values in paranthesis.A function can also store values as shown below:
# def greet(name):
#     gr="Hello"+name
#     return gr
# a=greet("Vaishnavi")
def mysum(num1,num2):
    return num1+num2
print(mysum(6,6))

#DEFAULT PARAMETER/ARGUMENT-We can have a value as a default argument in function.
# def greet(name="stranger"):
#     print("heyyy "+name)
# greet("Viahnavi")
# greet()    






