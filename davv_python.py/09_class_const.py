# define a class with multiple variable and get them printed 
class Student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
# instantiating the class 
dbase=Student(182,"sam",13)
print("roll no. of the student",dbase.id)
print("name of the student",dbase.name) 
print("age of the student",dbase.age)
