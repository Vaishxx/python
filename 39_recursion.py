# A function calling itself is called as recursion 

def fact_recursive(n):
    if n==0 or n==1: #-->based on the function which doesn't call the function any further
        return 1
    else:
        return n * fact_recursive(n-1) #-->function calling itself
print(fact_recursive(4))

# working:
# factorial(4)
#   |
#  4 x [factorial(3)]
#        |
#        3 x [factorial(2)]
#              |
#              2 x [factorial(1)]
# 4 x 3 x 2 x [1][factorial returned]
           
