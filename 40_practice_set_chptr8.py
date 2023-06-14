# wap using function to find greatst of 3 no.
# def max(num1,num2,num3):
#     if num1>num2 and num1>num3:
#         return num1
#     elif num2>num1 and num2>num3:
#         return num2
#     else:
#         return num3
# print(max(14,46,59))    

# wap to convert celcius into fahrenheit
# def converter(celcius):
#     celcius=(celcius*9/5)+32
#     return celcius
# print(converter(12),"F")

#How do you prevent a python print() function to print the new line at the end?
# print("Hello",end=" ")
# print("how",end=" ")
# print("are",end=" ")
# print("you?",end=" ")

#write a recursive function to calculate the sum of first n natural no.
# def sum_recursive(n):
#     if n==0:
#         return 0
#     else:
#         return sum_recursive(n-1)+n
# print(sum_recursive(10))    


#wap to print following pattern using function
# * * *
# * * 
# * 
# def pattern(n):
#     for i in range(n):
#         print('* '*(n-i))      
# pattern(3)    


#wap to remove a given word from the string and strip it at the same time.
def remove_and_strip(string,word):
    newstring=string.replace(word,"")
    return newstring.strip()

str="   vaishahahaha is a good gurl   "
print(remove_and_strip(str,"good"))    
