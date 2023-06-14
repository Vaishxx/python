#if__name__=='__main__'in py
#__name__ evaluates to the name of the module in py from where the program is ran.
#is thr module is being run directly from the commmand line,the __name__ is set to string '__main__'.Thus this behavior is used to check whether the module is run directly or imported to another file.
def greet(name):
    print('Good Evening,' ,name)
if __name__=='__main__':    
    n=input("name:")
    greet(n)    