"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 19:58:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 19:58:00
@Title : Write a Python program to calculate the length of a string.
"""
from Log import Log

def stringLength():
    """
    Description:
        this function calculate length of string
    """ 
    nameString = "swapnil"
    Log.logger.info(len(nameString))

stringLength()
