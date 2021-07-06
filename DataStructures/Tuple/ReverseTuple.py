"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 18:14:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 18:14:00
@Title : Write a Python program to reverse a tuple.
"""

from Log import Log

def reverseTuple():
    """
    Description: 
    this function reverse the tuple
    """
    nameTuple = ("swapnil")
    reverseTuple = tuple(reversed(nameTuple))
    Log.logger.info(reverseTuple)

reverseTuple()