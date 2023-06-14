class Employee:
    company="camel"
    salary=1000
    @classmethod
    def changesalary(cls,sal):
        cls.salary=sal

e=Employee()
print(e.salary)
e.changesalary(3456)
