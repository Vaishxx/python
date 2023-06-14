# wap to store 7fruits in a list entered by a user 
fruits=[]
f=input("enter first fruit name ")
f1=input("enter second fruit name ")
f2=input("enter third fruit name ")
f3=input("enter fourth fruit name ")
f4=input("enter fifth fruit name ")
f5=input("enter sixth fruit name ")
f6=input("enter seventh fruit name ")
fruits=[f1,f2,f3,f4,f5,f6]
print(fruits)

# wap to accept marks of 6 students and display them in sorted order

s1=int(input("enter marks of stud1 "))
s2=int(input("enter marks of stud2 "))
s3=int(input("enter marks of stud3 "))
s4=int(input("enter marks of stud4 "))
s5=int(input("enter marks of stud5 "))
s6=int(input("enter marks of stud6 "))
stud=[s1,s2,s3,s4,s5,s6]
stud.sort()
print(stud)

# wap to sum a list of 4 no. 
l1=[11,22,33,44]
print(l1[0]+l1[1]+l1[2]+l1[3])
# or
print(sum(l1))

# wap to count no. of zeroes in the following tuple
# a=(7,0,8,0,0,9)
a=(7,0,8,0,0,9)
print(a.count(0))


