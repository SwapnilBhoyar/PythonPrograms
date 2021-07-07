"""
@Author: Swapnil Bhoyar
@Date: 2021-07-07 10:05:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-07 10:05:00
@Title : Write a Python program to reverse a string.
"""

from Log import Log

def reverseString():
    """
    Description:
        this function reverse a string
    """
    txt = "Hello World"[::-1]
    Log.logger.info(txt)

reverseString()