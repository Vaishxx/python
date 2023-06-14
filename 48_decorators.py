#PYHTON DECORATORS-allows us to modify the behavior of the function and methods.
#-way to extend the functionality of the function or method without modifying its source code.
#-takes another function as an arg and returns a new function that modifies thr behavior of the original function.
#-the new function is called as the decorator function. 

def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("Thanks for using this function")
        return mfx
    return fx

@greet
def hello():
    print("hello world") 
hello() 
#greet(hello)()

            