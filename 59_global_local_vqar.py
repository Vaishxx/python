a=56
def func1():
    global a #will print global variable of a when called otherwise will print the local variable only
    print(a)
    a=8  #local variable
    print(a)
func1() 
print(a)   