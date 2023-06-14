while(True):
     print("press q to quit")
     a=input("enter a no.:" )
     if a=="q":
        break
     try:
        a=int(a)
        if a>6:
            print("you entered a no. greater than 6")
     except Exception as e:
        print("your input resulted in an error",e)
print("thanks for playing this game")
            