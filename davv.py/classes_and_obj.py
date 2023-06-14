class Student:
    name="vaishnavi"
    course="mtech"
    college="DAVV"

print(Student.name)
a=Student()
print(a.college)

class Emp:
    pass
vinod=Emp()
rahul=Emp()
print(vinod,rahul)

vinod.name="vinod"
vinod.section="marketing"
vinod.salary="10000000"
vinod.city="indore"
print(vinod.name)
print(vinod.section)
print(vinod.salary)
print(vinod.city)

rahul.name="rahul"
rahul.section="HR"
rahul.salary="2000000"
rahul.city="indore"
print(rahul.name)
print(rahul.section)
print(rahul.salary)
print(rahul.city)

print(vinod.__dict__)

class Mobile:
    def config():
        print("iphone","16 gb","128 gb")

mobile=Mobile
print(type(mobile))
mobile.config()


