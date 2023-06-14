# Python defines a set of functions that are used to generate or manipulate random numbers through the random module. eg-
import random
num = random.random()
print(num)
#-----------------------------------------------
# Different ways to Generate a Random Number in Python
# Method 1: Generating random number list in Python choice()
# Python3 program to demonstrate the use of
# choice() method

# import random
import random

# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))

# prints a random item from the string
string = "striver"
print(random.choice(string))
#------------------------------------------------------

# Method 2: Generating random number list in Python randrange(beg, end, step)
# Python code to demonstrate the working of
# choice() and randrange()

# importing "random" for random operations
import random

# using choice() to generate a random number from a
# given list of numbers.
print("A random number from list is : ", end="")
print(random.choice([1, 4, 8, 10, 3]))

# using randrange() to generate in range from 20
# to 50. The last parameter 3 is step size to skip
# three numbers when selecting.
print("A random number from range is : ", end="")
print(random.randrange(20, 50, 3))

# Method 3: Generating random number list in Python using seed()

# Method 4: Generating random number list in Python using shuffle()
import random
# declare a list
sample_list = ['A', 'B', 'C', 'D', 'E']

print("Original list : ")
print(sample_list)

# first shuffle
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)

# second shuffle
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)
#---------------------------------------------------------
# Method 5: Generating random number list in Python using uniform()
