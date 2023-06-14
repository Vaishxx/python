# concatenating two string
# greeting="good morning "
# name="vaishnavi"
# a= greeting+name
# print(a)

name="VAISHNAVI"
print(name[0])
print(name[4])
# name[2]="D" --> this will not work.we cant change the string element

# slicing     
print(name[0:4])  #-->this will print value upto n-1 terms
print(name[1: ])
print(name[:]) #-->will print the whole string from start to end

# indexing in a string array
#  0  1  2  3  4  5  6  7  8
#  V  A  I  S  H  N  A  V  I 
# -9 -8 -7 -6 -5 -4 -3 -2 -1 -->indexing when done from last element.this is used when the length of the string array is unknown 
print(name[-4:-1])  #-->this will print n-1 terms

# slicing skip value 
# syntax: variable[intial value:final value:no. of values to be skipped]
print(name[0:8:2])   #--> will print the value after skipping every second value
print(name[1: :3])

