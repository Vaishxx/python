class Person():
    name="vaish"
    networth=10000000
    occupation="software developer"
    def info(self):                
        print(f'{self.name} is a {self.occupation}')
#SELF PARAMETER-The self parameter is the refrence to the current instance of the class ,and is used to access variables that belongs to the class        

a=Person()
print(a.name)
a.info()
a.name="Hahaha"   #changing the default name
a.occupation="accountant"
print(a.name,a.occupation)

b=Person()
b.name="Aish"
b.occupation="HR"
b.info()
