# STONE PAPER SCISSOR
import random
i=1
while i!=0:
    

    options=['stone','paper','scissor']
    player=input('Your turn: ')
    robot=random.choice(options)
    print(robot)

    if robot==player:
        print("Robot=0  You=0")  
    elif robot==options[0]:
        if player==options[2]:
            print("Robot:1   You:0")
        elif player==options[1]:
            print("Robot:0   You:1") 

    elif robot==options[2]:
        if player==options[0]:
            print("Robot:0   You:1")   
        elif player==options[1]:
            print("Robot:1   You:0")     
    elif robot==options[1]:
        if player==options[0]:
            print("Robot:1   You:0")
        elif player==options[2]:
            print("Robot:0   You:1")           
    
    i=int(input("Press 0 to exit :"))





