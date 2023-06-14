board=['-','-','-',
       '-','-','-',
       '-','-','-']
player1="X"
player2="0"
gamerunning=True
winner=True

def boardstructure(board):
    print(board[0],"|",board[1],"|",board[2])
    print("--|---|--")
    print(board[3],"|",board[4],"|",board[5])
    print("--|---|--")
    print(board[6],"|",board[7],"|",board[8])
boardstructure(board)    

def boardinput1(board):
    position=int(input("PLAYER1(Enter a no. from 1-9): "))
    if position>=1 and position<=9 and board[position-1]=='-':
        board[position-1]=player1
    else:
        print("oops!The position has already been occupied")  

def boardinput2(board):
    position=int(input("PLAYER2(Enter a no. from 1-9): "))
    if position>=1 and position<=9 and board[position-1]=='-':
        board[position-1]=player2
    else:
        print("oops!The position has already been occupied")


def logic(board,count):
    #horizintal
    if board[0] == board[1]==board[2] and board[0]!= '-':
        print("WINNER!")
        return False
    elif board[3]==board[4]==board[5] and board[3]!= '-':
        print("WINNER!")
        return False
    elif board[6]==board[7]==board[8] and board[6]!= '-':  
        print("WINNER!") 
        return False
    #row
    elif board[0]==board[3]==board[6] and board[0]!= '-': 
        print("WINNER!")
        return False
    elif board[1]==board[4]==board[7] and board[1]!= '-': 
        print("WINNER!")
        return False
    elif board[2]==board[5]==board[8] and board[2]!= '-': 
        print("WINNER!")
        return False
    
    #diagonal
    elif board[0]==board[4]==board[8] and board[0]!= '-': 
        print("WINNER!")
        return False
    elif board[6]==board[4]==board[2] and board[6]!= '-': 
        print("WINNER!")
        return False  

    elif count ==  9:
        print('tie')  
    else:
        return True
count = 0
while gamerunning:

    count += 1
    boardinput1(board)
    boardstructure(board)
    gamerunning = logic(board,count)
    boardinput2(board)
    boardstructure(board) 
    gamerunning = logic(board,count)
     
print("Thanks for Playing,Hope You Enjoyed!")




