class Person():
    def __init__(self,n,occ):
        print("hey this is a constructor")
        self.name=n 
        self.occupation=occ

    def info(self):
         print(f"{self.name} is a {self.occupation}")

a=Person("vaish","developer")
b=Person("hahaha","singer")
a.info()
b.info()
