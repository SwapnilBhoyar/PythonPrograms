"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 17:58:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 17:58:00
@Title : Write a Python program to convert a list to a tuple.
"""

from Log import Log

def listToTuple():
    """
    Description:
        this function convert list to tuple
    """
    tempList = ['swapnil', 23, 3.4]
    tempTuple = tuple(tempList)
    Log.logger.info(tempTuple)

listToTuple()