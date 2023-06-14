#Q.1)Wap to enter string using input() function.
# name=input("Enter your name:")
# print("Hello ",name)
# print(type(name))

#Q.2)Wap to show the use of int() function for entering integer input.

car=input("Name of car:")
cost=int(input("Cost of car:"))
tax=int(input("Enter tax:"))
print(f'Your car is {car} and it overall cost is {cost+tax}/-Rs.')

#Q.3)Wap to use float() to accept float value from the user.
# a=float(input("Enter any value:"))
# b=float(input("Enter any value:"))
# summ=a+b
# print(summ)
# print(type(summ))

#Q.4)Wap to create fibonacci series.
#0 1 1 2 3 5 8 13 21...
# num=int(input("Enter no. of terms for series:"))
# a,b=0,1
# print(a,"",b,end=" ")
# for i in range(1,num+1):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c
# print("\nDone")  
# print(num-1)

#Q.5)Input sum of series.
n=int(input("Enter the value of n:"))
summ=0
for i in range (1,n+1):
    summ=summ+i
print("the total sum is",summ)
print("finished task!")

#Q.6)Wap to form a table of given no.
# num=int(input("Enter a no. for table:"))
# for i in range(1,11):
#     print(num,"X",i,"=",num*i)
# print("task finished!")

#Q.7) Create a function with the arguments and with return statement to calculate the area of square, circle ,rectangle and triangle.
# from math import pi

# def square(side):
#     return side*side
# def triangle(base,height):
#     return (1/2)*base*height
# def circle(radius):
#     return pi*radius*radius
# def rectangle(length, breadth):
#     return length*breadth

# print("Area of square is",square(4))
# print("Area of triangle is",triangle(10,40))
# print("Area of circle is",circle(11))
# print("Area of rectangle is",rectangle(4,36))

#Q.8)Create a program to print even no. number in a range in the form of a list.
# num = int(input("Last no of the series: "))
# even = list()
# for i in range (0,num + 1,2):
#     even.append(i)
# print(even)


#Q.9)Program to create a dictionary,where keys are no. and values are their cubes,entering last no. through user input.
# num = int(input("Last no of the series: "))
# DictOfCube = dict()
# for i in range (1,num + 1,):
#     DictOfCube[i] = i**3
# print(DictOfCube)

#Q.10)Create a data of your own having 20 rows and 5 columns.The data should be meaningful.Now use pandas to read the data.Use Info(),Describe(),head and Tail function to show the data.Now use matplot lib and plot the following,
#1.line graph between the first column and all the 4 column respectively.
#2.Bar graph with some details.
#3.Scatter plot with some details.
#Plot a subplot also using (3)point.






