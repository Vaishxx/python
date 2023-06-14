# F=friends
# L=Lovers
# A=Affectionate
# M=Marriage
# E=Enemies
# S=Siblings

choice=1
while choice!=0:
    name1=input("First Person's Name: ")
    name2=input("Second Person's Name: ")
    
    count=0
    l1=len(name1)+len(name2)
    for i in range(len(name1)):
        pass
        for j in range(len(name2)):   
            if name1[i]==name2[j]: #name1[0]==name2[6]
                cancelled_letter=name2[j] #name2[6]
                
                name2=name2[:j]+name2[j+1:]
                # print(name2)
                    
                count=count+1
                # print(count)  
                break
            
        
    count=2*count
    l1=l1-count-1
    # print(l1)

    flames=['FRIENDS','LOVERS','AFFECTIONATE','MARRIAGE','ENEMIES','SIBLINGS']
    if l1<6:
        print(flames[l1])
    else:
        l1=int(l1%6)
        print(flames[l1]) 
    try:      
        choice=int(input("PRESS 0 FOR EXIT:"))
        if choice==0:
            print("THANKS FOR PLAYING THIS GAME!😊")   
    except Exception as e:
        if choice!=int(choice):
            print("PLEASE ENTER AN INTEGER TYPE VALUE")    
             