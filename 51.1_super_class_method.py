class Person:
    def take_breath(self):
        print("i am breathing")

class Employee(Person):
    company="honda"        
    def take_breath(self):
        print("i am an employee and i luckily can breath")

class Programmer(Employee):
    def take_breath(self):
        super().take_breath()  #iski parent class ka value return krta hai ye
        print("i am a programmer so i am also breathing")

p=Person()
p.take_breath()

e=Employee()
e.take_breath()

pr=Programmer()
pr.take_breath()

'''
super()__init__() -------->calls constructor of the base class'''
