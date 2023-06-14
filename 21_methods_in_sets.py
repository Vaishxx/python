a={1,2,3,4,5}
#add
a.add(10) #set.add takes 1 argument
a.add(20)
a.add(10)
a.add(10)
a.add(20)  #doesnt metter how many times youy add the same element,it will show only one time
print(a)

# ADD METHOD
# adding list in set 
# a.add([45,56,67]) #throws an error i.e unhashable type of list it is beacuse content of list can be change unlike sets content
# print(a)

# adding tupple in set 
# we can add tupple in set 
a.add((23,45,67))
print(a)

# we cant add dictionary in set coz it is unhashable i.e its content is changeable unlike sets 
# a.add({4:5}) #throws an error

# LEN METHOD
print(len(a)) #will print the length of the set

# REMOVE METHOD
a.remove(5)
print(a)

# POP METHOD
print(a.pop()) #removes an arbitrary element from the the set and returns the element removed
print(a)

# CLEAR SET METHOD
# print(a.clear()) #empties the set

# UNION METHOD
print(a.union({11,22,33})) #returns the union of both the sets

# INTERSECTION METHOD
print(a.intersection({2,3,10,20})) #will print the intersection of both the sets
