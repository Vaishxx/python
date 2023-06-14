#wap to display a/b where a and b are integers. If b=0 , display infinte by hadling the ZeroDivisionError.
a=int(input("a= "))
b=int(input("b= "))
try:
    print(a/b)
except ZeroDivisionError as e:
    if b==0:
        print("infinte")        