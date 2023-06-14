input("Student Name:")
input("Course:")
input("Semester:")



print("---------------------MATHEMATICS-3-------------------------")
#internals
test1=int(input("marks scored in test1:"))
test2=int(input("marks scored in test2:"))
test3=int(input("marks scored in test3:"))

if(test1<test2 and test1<test3):
    internalmarks1=test2+test3
    print("Total Internal marks:",internalmarks1)
elif(test2<test1 and test2<test3):
    internalmarks1=test1+test3
    print("Total Internal marks:",internalmarks1)    
else:
    internalmarks1=test1+test2
    print("Total Internal marks:",internalmarks1)
 
#endsem
endsem_maths=int(input("End sem marks:"))
#totalmarks
total_0=endsem_maths+internalmarks1
print("Total marks scored in Mathematic-3:",total_0)

print("---------------COMPUTER-ARCHITECTURE-------------------------")
#internals
test1=int(input("marks scored in test1:"))
test2=int(input("marks scored in test2:"))
test3=int(input("marks scored in test3:"))

if(test1<test2 and test1<test3):
    internalmarks2=test2+test3
    print("Total Internal marks:",internalmarks2)
elif(test2<test1 and test2<test3):
    internalmarks2=test1+test3
    print("Total Internal marks:",internalmarks2)    
else:
    internalmarks2=test1+test2
    print("Total Internal marks:",internalmarks2)
 
#endsem
endsem_ca=int(input("End sem marks:"))
#totalmarks
total_1=endsem_ca+internalmarks2
print("Total marks scored in Computer Architecture:",total_1)

print("--------------DESIGN AND ANALYSIS OF ALGORITHM-------------------")
#internals
test1=int(input("marks scored in test1:"))
test2=int(input("marks scored in test2:"))
test3=int(input("marks scored in test3:"))

if(test1<test2 and test1<test3):
    internalmarks3=test2+test3
    print("Total Internal marks:",internalmarks3)
elif(test2<test1 and test2<test3):
    internalmarks3=test1+test3
    print("Total Internal marks:",internalmarks3)    
else:
    internalmarks3=test1+test2
    print("Total Internal marks:",internalmarks3)
 
#endsem
endsem_daa=int(input("End sem marks:"))
#totalmarks
total_2=endsem_daa+internalmarks3
print("Total marks scored in Design and Analysis of Algorithm",total_2)

print("--------------------NUMERICAL METHODS-------------------------")
#internals
test1=int(input("marks scored in test1:"))
test2=int(input("marks scored in test2:"))
test3=int(input("marks scored in test3:"))

if(test1<test2 and test1<test3):
    internalmarks4=test2+test3
    print("Total Internal marks:",internalmarks4)
elif(test2<test1 and test2<test3):
    internalmarks4=test1+test3
    print("Total Internal marks:",internalmarks4)    
else:
    internalmarks4=test1+test2
    print("Total Internal marks:",internalmarks4)
 
#endsem
endsem_nm=int(input("End sem marks:"))
#totalmarks
total_3=endsem_nm+internalmarks4
print("Total marks scored in Numerical Methods:",total_3)

print("----------------OBJECT ORIENTED PROGRAMMING-------------------")
#internals
test1=int(input("marks scored in test1:"))
test2=int(input("marks scored in test2:"))
test3=int(input("marks scored in test3:"))

if(test1<test2 and test1<test3):
    internalmarks5=test2+test3
    print("Total Internal marks:",internalmarks5)
elif(test2<test1 and test2<test3):
    internalmarks5=test1+test3
    print("Total Internal marks:",internalmarks5)    
else:
    internalmarks5=test1+test2
    print("Total Internal marks:",internalmarks5)
 
#endsem
endsem_oops=int(input("End sem marks:"))
#totalmarks
total_4=endsem_oops+internalmarks5
print("Total marks scored in Object Oriented Programming:",total_4)

print("-----------------PROBABILITY DISTRIBUTION-------------------")
#internals
test1=int(input("marks scored in test1:"))
test2=int(input("marks scored in test2:"))
test3=int(input("marks scored in test3:"))

if(test1<test2 and test1<test3):
    internalmarks6=test2+test3
    print("Total Internal marks:",internalmarks6)
elif(test2<test1 and test2<test3):
    internalmarks6=test1+test3
    print("Total Internal marks:",internalmarks6)    
else:
    internalmarks6=test1+test2
    print("Total Internal marks:",internalmarks6)
 
#endsem
endsem_prob=int(input("End sem marks:"))
#totalmarks
total_5=endsem_prob+internalmarks6
print("Total marks scored in Probability Distribution:",total_5)

print("---------------------COMPREHENSIVE-VIVA---------------------")
total_6=int(input("Points in Comprehensive Viva:"))

print("*************************CREDITS*******************************")
total=[total_1,total_2,total_3,total_4,total_5,total_6]
i=0
while i<6:
    if total[i]>=90:
        print("Grade=O")
        points=10
    elif total[i]>=80:
        print("Grade=A+")
        points=9
    elif total[i]>=70:
        print("Grade=A")
        points=8
    elif total[i]>=60:
        print("Grade=B+")
        points=7
    elif total[i]>=50:
        print("Grade=C")
        points=6 
    elif total[i]>=40:
        print("Grade=D")
        points=5 
    else:
        print("Grade=F")
    i=i+1    
                
if total_6==10:
        print("Grade=O")
elif total_6==9:
        print("Grade=A+")       
elif total_6==8:
        print("Grade=A")      
elif total_6==7:
        print("Grade=B+")        
elif total_6==6:
        print("Grade=C")        
elif total_6==5:
        print("Grade=D")        
else:
        print("Grade=F")
       
              








