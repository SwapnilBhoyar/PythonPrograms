"""
@Author: Swapnil Bhoyar
@Date: 2021-06-29 19:15:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-06-29 19:15:00
@Title: Simulate gambler game
"""
import random

BET_count = 0
BET_WINS = 0

def getRandomValue():
    """
    Description:
        this function is used to random value
    Return:
        this function return a random value 0 or 1
    """
    value = random.randint(0, 1) 
    return value

def gamble(Stake, Goal):
    """
    Description:
        this function determine player won or loss
    Parameters:
        Stake: contain int value
        Goal: conatin int value
    Return:
        return 0 or 1
    """
    global BET_count
    global BET_WINS
    
    while(Stake > 0 and Stake < Goal):
        play = getRandomValue()
        if play == 1:
            Stake += 1
            BET_WINS += 1
        else:
            Stake -= 1
        BET_count += 1

    print("Bet wins:", BET_WINS)
    print("Bet count:", BET_count)

    if(Stake == 1):
        return 1
    else:
        return 0

def playGame(Stake, Goal, numberOfTimes):
    """
    Description:
        this function give number of game player won
    Parameter:
        Stake: contain int value
        Goal: conatin int value
    """
    GAME_COUNT = 0
    GAME_WON = 0
    GAME_LOST = 0

    while(GAME_COUNT < numberOfTimes):
        print("Game:", GAME_COUNT)
        result = gamble(Stake, Goal)

        if result == 1:
            GAME_WON += 1
        else:
            GAME_LOST += 1
        
        GAME_COUNT += 1

    print("Number of games won:", GAME_WON)

    winPercentage = GAME_WON / GAME_COUNT * 100
    lossPercentage = 100 - winPercentage

    print("Winning percentage is:", winPercentage)
    print("Lossing percentsge is:", lossPercentage)

Stake = int(input("Enter stake value:"))
Goal = int(input("Enter goal value:"))
numberOfTimes = int(input("Enter number of times want to play:"))

playGame(Stake, Goal, numberOfTimes)