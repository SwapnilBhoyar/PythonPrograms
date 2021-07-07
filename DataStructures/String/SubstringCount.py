"""
@Author: Swapnil Bhoyar
@Date: 2021-07-07 9:59:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-07 09:59:00
@Title : Write a Python program to count occurrences of a substring in a string.
"""

from Log import Log

def substringCount():
    """
    Description:
        this function count substring
    """
    tempString = 'The quick brown fox jumps over the lazy dog.'
    Log.logger.info(tempString.count("fox"))

substringCount()