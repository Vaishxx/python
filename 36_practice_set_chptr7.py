# Q1 wap to print multiplication table for a given no. using for loop
# num=int(input("Enter a number:"))
# for i in range(1,11):
#     a=i*num
#     # print(num,"X",i,"=",a)
#     # print(str(num)+"X"+str(i)+"="+str(a))
#     print(f"{num}X{i}={a}")  #called as f string
#     i=i+1


#Q2 wap to greet all the person's name stored in the list l1 which starts from S 
# l1=["harry","Soham","Sachin","Rahul"]
# l1=["harry","Soham","Sachin","Rahul"]
# for name in l1:
#     if name.startswith("S"):
#         print("Good morning "+name)
    

# Q3 wap to check whether the given no. is prime or not 
# num=int(input("Enter a number:"))
# i=2
# while i<num/2:
#     if num%i==0:
#         print(num," is not Prime no.")
#         break   
#     i=i+1
# else:
#         print(num," is a Prime no.")    


#Q4 wap to find the sum of first n natural no. using while loop 
# num=int(input("Enter a number: "))

# i=1
# sum=0
# while i<=num:
#     sum=sum+i
#     i=i+1
# print(sum)

# Q5 wap to find factorial of n 
# n=int(input("Enter a number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     i=i+1
# print(f"Factorial of {n} is:{fact}")    


# Q6 wap to print the following star pattern 
    #          *
    #          * *
#              * * *
            #  * * * *
for i in range(4):
    print("* "*(i+1))


#Q7 wap to print the following star pattern 
#                *
#              * * *
#            * * * * * 
#          * * * * * * * 
n=4
for i in range(n):
    for j in range(n-i):
        print('* ')
        j=j+1
    i=i+1    




