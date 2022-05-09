from random import Random
from tabnanny import check
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
import sys
import random
sys.setrecursionlimit(2000)
# sign variable to decide the turn of which player
sign = 0
  
# Creates an empty board
global board
board = [[" " for x in range(3)] for y in range(3)]



def winner(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))


def checkWon(board,mark):
    if board[0] == board[1] and board[0] == board[2] and board[0] == mark:
        return True
    elif (board[3] == board[4] and board[3] == board[5] and board[3] == mark):
        return True
    elif (board[6] == board[7] and board[6] == board[8] and board[6] == mark):
        return True
    elif (board[0] == board[3] and board[0] == board[6] and board[0] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[0] == board[4] and board[0] == board[8] and board[0] == mark):
        return True
    elif (board[6] == board[4] and board[6] == board[2] and board[6] == mark):
        return True
    else:
        return False




  
# Check if the player can push the button or not
def isfree(i, j):
    return board[i][j] == " "
  
# Check the board is full or not
def isfull():
    flag = True
    for i in board:
        if(i.count(' ') > 0):
            flag = False
    return flag
  


  
# Decide the next move of system
def checkDraw(board):
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

def PC():
    
    board1={0: board[0][0], 1: board[0][1], 2: board[0][2],
         3: board[1][0], 4:board[1][1], 5:board[1][2],
         6: board[2][0], 7: board[2][1], 8: board[2][2]}
   
    bestScore = -800
    bestMove = 0
    for key in board1.keys():
        if (board1[key] == ' '):
            board1[key] = 'O'
            score = minimax(board1,False)# tiến hành backtrack liên tục đến khi về lại state ban dau
            board1[key] = ' '
            #print(score)
            if (score > bestScore):
                bestScore = score
                bestMove = key
    #printBoard(board1)
    return (int(bestMove/3),int(bestMove%3))

def minimax(board1,isMaximizing):
    if (checkWon(board1,'O')):          #nếu mà bot thắng thì return 1
        return 1
    elif (checkWon(board1,'X')):        # nếu mà player thắng thì return -1
        return -1
    elif (checkDraw(board1)):            #tie =0
        return 0

    if (isMaximizing):                      # nếu maximizing true thì bot chạy
        bestScore = -800
        for key in board1.keys():
            if (board1[key] == ' '):
                board1[key] ="O"
                score = minimax(board1, False)
                board1[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:                                       # nếu maximizing false  thì player chạy 
        bestScore = 800
        for key in board1.keys():
            if (board1[key] == ' '):
                board1[key] = 'X'
                score = minimax(board1,True)
                board1[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore

# Configure text on button while playing with system
def playerPlayFirst(i, j, gb, l1, l2):# nếu player chơi trước
    global sign
   
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"

           
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"

            
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
    elif(isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
    if(x):#check turn ( pc or player)
        if sign % 2 != 0:
            move = PC()
            button[move[0]][move[1]].config(state=DISABLED)
            playerPlayFirst(move[0], move[1], gb, l1, l2)

def robotPlayFirst(i, j, gb, l1, l2):#bot choi truoc
    global sign
   
    if board[i][j] == ' ':
        if sign % 2 == 1:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"

           
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"

            
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
    elif(isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
    if(x):#check turn ( pc or player)
        if sign % 2 == 0:
            move = PC()
            button[move[0]][move[1]].config(state=DISABLED)
            robotPlayFirst(move[0], move[1], gb, l1, l2)
# Create the GUI of game board for play along with system
def randomFirstPosition():#random vi tri dau tien khi may tinh choi tr
    return int(random.randint(0,2)),random.randint(0,2)


def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(playerPlayFirst, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board, bd=5,command= get_t ,height=4, width=8)
            button[i][j].grid(row=m, column=n)
           #button[1][1]='O'
    
    game_board.mainloop()


def gameboard_pc1(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(robotPlayFirst, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board, bd=5,command= get_t ,height=4, width=8)
            button[i][j].grid(row=m, column=n)
            #button[1][1]='O'
    position=randomFirstPosition()
    button[position[0]][position[1]].config(state=DISABLED)
    robotPlayFirst(position[0], position[1], game_board, l1, l2)
    game_board.mainloop()


# Initialize the game board to play with system
def graphicTicTacToe(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text = "Computer : O",
                width = 10, state = DISABLED)
      
    l2.grid(row = 2, column = 1)

    gameboard_pc(game_board, l1, l2)
  

def graphicTicTacToe1(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text = "Computer : O",
                width = 10, state = DISABLED)
      
    l2.grid(row = 2, column = 1)

    gameboard_pc1(game_board, l1, l2)


# main function
def play():
    menu = Tk()
    menu.geometry("250x114")
    menu.title("Tic Tac Toe")
    wpc = partial(graphicTicTacToe, menu)
    wpc1 = partial(graphicTicTacToe1, menu)

    B1 = Button(menu, text = "Play(player ) ", command = wpc, 
                activeforeground = 'red',
                activebackground = "yellow", bg = "red", 
                fg = "yellow", width = 500, font = 'summer', bd = 5)
      
    B2 = Button(menu, text = "Play(robot) ", command = wpc1, 
                activeforeground = 'red',
                activebackground = "yellow", bg = "red", 
                fg = "yellow", width = 500, font = 'summer', bd = 5)
      
    B3 = Button(menu, text = "Exit", command = menu.quit, activeforeground = 'red',
                activebackground = "yellow", bg = "red", fg = "yellow",
                width = 500, font = 'summer', bd = 5)

    B1.pack(side = 'top')
    B2.pack(side = 'top')
    B3.pack(side = 'top')
    menu.mainloop()
  
# Call main function
if __name__ == '__main__':
    play()