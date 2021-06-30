"""
@Author: Swapnil Bhoyar
@Date: 2021-06-29 23:09:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-06-30 11:15:00
@Title: Write a Program to play a Cross Game or Tic-Tac-Toe Game. Player 1
is the Computer and the Player 2 is the user. Player 1 take Random Cell that is
the Column and Row.
"""
import random

def print_board(a):
    """
        Description:
            this function is for display the tic tac toe board
        Parameter:
            a: list contain position value
    """
    print("",a[1]," │",a[2]," │ ",a[3]," ")
    print("────┼────┼────")
    print("",a[4]," │",a[5]," │ ",a[6]," ")
    print("────┼────┼────")
    print("",a[7]," │",a[8]," │ ",a[9]," ")
    
def print_instructions(players):
    """
        Description:
            this function is for display the instruction of game
        Parameter:
            player: list conatain player info as list
    """
    print("\n----------- WELCOME TO TIC TAC TOE ------------\n\n")
    print_board(pos)
    print()
    
    players[0] = "Computer"
    players[1] = input("Player 2 name: ")
    
    print("\n-------- Instructions ---------")
    print("->",players[0],"you will using 0")
    print("->",players[1],"you will using X")
    print("-> Turn starts from",players[0])
    print("-> Potisions are like :-")
    print("  1 │  2 │ 3  ")
    print("────┼────┼────")
    print("  4 │ 5  │ 6  ")
    print("────┼────┼────")
    print("  7 │ 8  │ 9  ")  

def getPosition(pos):
    """
        Description:
            this function calculate random value
        Parameter:
            pos: list contain pos info
        Return:
            randomValue: int
    """
    randomValue = random.randint(1, 9)
    if pos[randomValue] == '0' or pos[randomValue] == 'X':
        randomValue = getPosition(pos)
    return randomValue
        
def startgame(pos):
    """
        Description:
            simulate game 
        Parameter:
            pos: consist pos info
    """
    turn = 0
    for i in range(9):
        if turn % 2 == 0:
            v = '0'
            print("\nthis is ur turn",players[0])
            p = getPosition(pos)
            pos[p] = v
            print_board(pos)
            winner = checkwin(v)
            if winner == "nobody":
                turn = 1
                continue
            else:
                print("\n\nCongratulations !!,",players[0]," win")
                break
        else:
            print("\nthis is ur turn",players[1])
            p = int(input("Please Enter postion : "))
            v = 'X'
            pos[p] = v
            print_board(pos)
            winner = checkwin(v)
            if winner == "nobody":
                turn = 0
                continue
            else:
                print("\n\nCongratulations !!,",players[1]," win")    
                break
    else:
        print("\n\nGame is Tie")
        
def checkwin(v):
    """
        Description:
            this function check for winner 
        Parameter:
            v: character 0 or X
        Return:
            winner : int
        """
    for i in winning_conditions:
        if (pos[i[0]], pos[i[1]], pos[i[2]]) == (v,v,v):
            winner = players[0]
            break
        elif (pos[i[0]], pos[i[1]], pos[i[2]]) == (v,v,v):
            winner = players[1]
            break
    else:
        winner = "nobody"
    return winner

pos = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
players = ['','']
winning_conditions = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
print_instructions(players)
startgame(pos)
