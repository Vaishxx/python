class Person():
    """below line is called as dunder method which is used to form a constructor.we have to use __init__(self)to form a constructor."""
    def __init__(self):
        print("hey this is a constructor")

    # def info(self):
    #     print(f"{self.name} is a {self.occupation}")

a=Person()
b=Person()

# a.name="vaish"
# a.occupation="developer"
# a.info()

#TYPES OF CONSTRUCTOR:-
'''1.PARAMETERIZED CONSTRUCTOR-when the constructor accepts arg along with self,it is known as parametrized constructor

2.DEFAULT CONSTRUCTOR-when the constructor doesn't accept any arg from the obj and has only 1 arg ,self,in the constructor ,it is known as default constructor'''

        