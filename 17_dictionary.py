# chapter 5
# DICTIONARY:collection of key value pairs 
# syntax:
#   a={"key": "value",
#       "code":"python",
#       "marks":"100",
#       "list":[1,2,3,4] }
mydict={ "vaish": "a coder",                
          "course": "mtech ai and ds dual degree",
          "anotherdict":{"school": "chameli devi public school"  #this is dictionary inside a dictionary}
                         }
        }#this is a dictionary
print(mydict["vaish"]) 
print(type(mydict["vaish"])) 
print(mydict["course"])
print(mydict["anotherdict"]["school"])