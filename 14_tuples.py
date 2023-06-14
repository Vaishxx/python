#A tuple is the immutable(unchangeable) type of data type in python....these are kind of list but the difference is that we cant update the values in tuple
# also tuples are created by using paranthesis brackets()

t=(1,4,6,8,10)  
print(t[0])   #printing value of tuple

#cannot update the value of tuple
# t[0]=34
print(t)   #gives error
#  tupple does not support item assignment

# t=()  -->empty tuple
t=(1,) #-->tuple with only single element (needs a comma)
# t=(1) wrong way to delcare a tupple with a single element
# t=(1,7,2) -->tuple with more than one element