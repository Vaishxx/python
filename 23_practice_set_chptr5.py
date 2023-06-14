#wap to create a dictionary of hindi words with values as their english translation.provide user as an option to look up 
dict={ 
    "flower":"phool",
    "water" :"pani",
    "mountain":"pahadh"
}
word=input("enter the word which you want to find\n") #without \n it will throw error
print(dict.get(word))

#wap to input 8 no. from user and display all the unique no. once

a1=int(input("enter the value\n"))
a2=int(input("enter the value\n"))
a3=int(input("enter the value\n"))
a4=int(input("enter the value\n"))
a5=int(input("enter the value\n"))
a6=int(input("enter the value\n"))
a7=int(input("enter the value\n"))
a8=int(input("enter the value\n"))
a={a1,a2,a3,a4,a5,a6,a7,a8}
print(a)

#can we print int 18 and str 18 in set.will it return only one 18 or both?
#ans) s{18,"18"} no,it will return both the 18 as both have differenet datatype 

#what will be length of the following set: s={20,20.0,"20"}
# ans)2 
s={20,20.0,"20"}
print(len(s))

#create an empty dictionary.Allow 4 friends to enter their favourite language as values and their names as key.Assume that their names are unique.
mydict={}

a=input('enter your fav lang Ram\n')
b=input('enter your fav lang shyam\n')
c=input('enter your fav lang Radha\n')
d=input('enter your fav lang seeta\n')

mydict["ram"]=a 
mydict["shyam"]=b
mydict["radha"]=c
mydict["seeta"]=d
print(mydict)

# can we change the value of list which is inside a set s=(1,2,"vaish",[1,2])?
# firstly a set can never contain a list 
# if there would be a tuple rather than list then too we cant change as the values in tuple are unaccessible .also set doesnt support changing in the value.therefore we cant change any type of data in sets 
