"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 17:27:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 17:27:00
@Title : Write a Python program to create the colon of a tuple.
"""
from copy import deepcopy
from Log import Log

def createColon():
    """
    Description:
        this function use colon
    """
    #create a tuple
    tempTuple = ("HELLO", 5, [], True) 
    Log.logger.info(tempTuple)

    #make a copy of a tuple using deepcopy() function
    tuplexColon = deepcopy(tempTuple)
    tuplexColon[2].append(50)
    Log.logger.info(tuplexColon)

createColon()