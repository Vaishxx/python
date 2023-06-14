try:
    a=int(input('enter a no.:'))
    c=1/a
except ValueError as e:
    print("plese enter a correct value")
except ZeroDivisionError as e:
    print('make sure that the divisor should not be 0')    
print('thanks for playing this game')    
