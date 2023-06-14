def greet(fx):
    def mfx(*arg,**kwargs):  #'*' is used for tuple and '**' is used for dictionary
        print("good morning")
        fx(*arg,**kwargs)
        print("Thanks for using this function")
        return mfx
    

def add(a,b):
    return a+b
greet(add)(1,2)