
lang=["swift",'python','go','javascript']
# access items of a list using fot loop 
for lang in lang:
    print(lang)

quat=int(input("Enter quantity:"))
if quat>900:
    print("Excellent")
elif quat>750:
    print("good performance")  
elif quat>500:
    print("Average")      
else:
    print("poor performance")    
