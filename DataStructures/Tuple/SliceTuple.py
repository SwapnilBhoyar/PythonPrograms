"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 18:14:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 18:14:00
@Title : Write a Python program to slice a tuple.
"""

from Log import Log

def sliceTuple():
    """
    Description:
        this function slice the tuple
    """
    tempTuple = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
    sliceTuple = tempTuple[2:9:2]
    Log.logger.info(sliceTuple)

sliceTuple()