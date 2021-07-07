"""
@Author: Swapnil Bhoyar
@Date: 2021-07-07 10:14:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-07 10:14:00
@Title : Write a Python program to lowercase first n characters in a string.
"""

from Log import Log

def lowerFirstN():
    """
    Description:
        this function lower first n chars
    """
    string = 'LOWERFIRST4CHAR'
    Log.logger.info(string[:4].lower() + string[4:])
    
lowerFirstN()