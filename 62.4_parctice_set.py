#store the multiplication table generated in problem 3 in a file named as tables.txt
num=int(input('enter a no.:'))
list1=[i*num for i in range(1,11)]
print(list1)
with open('tables.txt','a') as f :
    f.write(str(list1))
    f.write('\n')