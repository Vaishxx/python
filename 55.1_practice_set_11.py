#create a class pets from a class animal and further create class dog from pets.add a method bark to the class dog
class Animal:
    def properties(self):
        print("I can walk")

class Pets(Animal):
    def properties(self):
        print("i can walk and i live in house")

class Dog(Pets):
    def properties(self):
        print("i can walk,i live in house and i bark")

ani=Animal()        
pet=Pets()
doggo=Dog()
doggo.properties()
