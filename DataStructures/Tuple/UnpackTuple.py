"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 15:42:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 15:42:00
@Title : Write a Python program to unpack a tuple in several variables.
"""
from Log import Log
def unpackTuple():
    """
    Description:
        this function unpack tuple
    """
    tempTuple = ("swapnil", 23, 2.3)
    stringValue, intValue, floatValue = tempTuple 
    Log.logger.info(stringValue)
    Log.logger.info(intValue)
    Log.logger.info(floatValue)


unpackTuple()

