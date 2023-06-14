'''1.)if bolean exprssion
   (statement will execute if condition true)

   2.)if (boolean expression)
   (standard will executev if boolean comnndition true)

   else
   (statement will execute if boolesan condition false)

   3.)if (boolean condition)
   (statement will execute if condition true)
     if (condition 2)
      executes when condtion 1 and condition 2,both true
     else
      executes when condition 2 if false

   else
    when condition ia false
    
   4.)if (boolean condition 1)
     (statemenet will execute if boolean condition 2 true) 
     elif(condition 3)

     else statement

     '''
x=int(input("Enter any no.: "))
if x>50:
    print("False,statemenet skippeds")
elif x>20:
    print("true,block executed")
elif x>10:
    print("true,but block will not exceute")        
else:
    print("If all fails.")    
      