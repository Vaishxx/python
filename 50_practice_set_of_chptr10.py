# create a class programmer for storing info of few programmer working at microsoft
class Programmer:
    company="microsoft"
    def __init__(self,name,occupation,salary):
        self.name=name
        self.occupation=occupation
        self.salary=salary
        print(name,occupation,salary)

emp1=Programmer('Vaish','Data Scientist',20000000)
emp2=Programmer('Shiv','HR',10000000)
emp3=Programmer('Aish','Software developer',1000000)
emp4=Programmer('Raman','Data Analytics',2000000)

