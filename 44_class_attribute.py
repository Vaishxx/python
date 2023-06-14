# CLASS ATTRIBUTES-belongs to a class rather than a particular object
# example-
class Employee():
    company="GOOGLE"   #(class attribute)specific to each class
vaish=Employee()       #object instantiation
harry=Employee()
print(vaish.company)
print(harry.company)
Employee.company="YOU TUBE"   #changing class attributes
print(vaish.company)
print(harry.company)
