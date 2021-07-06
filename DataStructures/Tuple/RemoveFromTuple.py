"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 18:06:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 18:06:00
@Title : Write a Python program to remove an item from a tuple.
"""

from Log import Log

def removeFromTuple():
    """
    Description:
        remove element from tuple
    """
    tempTuple = (12, 34, 56, 21)
    tempList = list(tempTuple)
    tempList.remove(12)
    tempTuple = tuple(tempList)
    Log.logger.info(tempTuple)

removeFromTuple()