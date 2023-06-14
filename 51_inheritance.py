#inheritance is a way of creating a new class from an existing class
'''
syntax:
class Employee:
   #code       --------->base class

class Programmer(Employee):
   #code       --------->derived class
'''
class Employee:
    company="google"
    def showdetails(self):
        print('this is an employee')
    
class Programmer(Employee):
    salary=10000000000
    def getdata(self):
        print("Vaish")

    def showdetails(self):  #overriding-in this the method is made in the child class also and when the same method is called from both the classes e.g showdetails() it will execute the method of child class
       print('this is a programmer')  
e=Employee()       
e.showdetails()
p=Programmer()
p.getdata()

print(p.company)
p.showdetails()


'''
TYPES OF INHERITANCE
1)single inheritance
2)Multiple inheritance
3)Multilevel inheritance
'''
