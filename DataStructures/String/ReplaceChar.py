"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 20:23:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 20:23:00
@Title : Write a Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.
"""
from Log import Log

def replaceChar():
    """
    Description:
        this function replace character with $
    """
    sampleString = "restart"
    char = sampleString[0]
    sampleString = sampleString.replace(char, '$')
    sampleString = char + sampleString[1:]

    Log.logger.info(sampleString)

replaceChar()

    