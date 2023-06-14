class Empployee:
    company="google"
    def info(self):
        print(f"this person's salary is {self.salary} ")
    
    @staticmethod
    def greet():   #apnko self srgument denee ki zrurt nhi pdegi jb apn static method decorator use kr rhe ho to
        print("good morning maam!")

emp=Empployee()
emp.salary=128726487
emp.info()
print(emp.company) 
emp.greet()      