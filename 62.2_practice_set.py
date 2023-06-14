#write a list comprhension to print a list that contains the multplication table of a user entered no.
num=int(input("enter a no.: "))
# for i in range(1,11):
#     print(f'{num} X {i} = {num*i}')
list1=[i*num for i in range(1,11)]
print(list1)