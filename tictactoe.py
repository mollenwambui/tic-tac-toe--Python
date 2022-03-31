#create the game board
#from ast import While
#from tkinter import W


board=["-","-","-",
       "-","-","-",
       "-","-","-"]
#take player in input
current_player="x"
winner=None
gamerunning=True

def printBoard(board):
    print(board[] + " | " + board[1] + " |"+ board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " |"+ board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " |"+ board[8])

def playerInput(board):
    inp= int(input("Enter a number 1-9: "))
    if  inp>=1 and inp<=9 and board [inp-1] == "-":
        board[inp-1] =current_player
    else:print("ooops player is already in that spot!")
#check win or tie
#switch the player
while gamerunning:
    printBoard(board)
    playerInput(input)
   # def checkhorizontal(board):5