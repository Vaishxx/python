# methods in dictionary 
mydict={ "name":"vaish",
         "course":"mtech dual degree ai and ds",
         "marks":[1,2,3,4],
         "anotherdict":{"hey":"you"},
         1: 2
    }
print(list(mydict.keys())) # will print all the keys in the form of list    
#print(type(mydict.keys()))  #its datatype is dict_keys by default
print(mydict.values())
print(mydict.items()) #returns the list of (keys,values) types  

newdict={ "ram":"friend",
              "shyam":"friend",
              "mohan":"friend" ,
              "marks":[10,20,30,40] #when the same key is used then it changes the previous value with the new one

}
mydict.update(newdict) #updates the dictionary by adding key-value pairs from new dictionary
print(mydict)

# similarity in printing a key value between [] syntax of dictionary  and get function method
print(mydict["name"]) #prints values asscociated with key "name"
print(mydict.get("name"))#prints values asscociated with key "name"

# difference in printing key value  
# print(mydict["name2"])  #throws an error as name2 is not present in mydict
print(mydict.get("name2")) #returns none as name2 is not present in mydict