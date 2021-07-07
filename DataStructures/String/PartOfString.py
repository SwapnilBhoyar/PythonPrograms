"""
@Author: Swapnil Bhoyar
@Date: 2021-07-07 9:31:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-07 09:31:00
@Title : Write a Python program to get the last part of a string before a specified character.
"""

from Log import Log

def partOfString():
    """
    Description:
        this function split the string
    """
    url = 'https://www.w3resource.com/python-exercises/string'
    #rsplit(separator, maxslpit)
    Log.logger.info(url.rsplit('/', 1)[0])
    Log.logger.info(url.rsplit('-', 1)[0])
    
partOfString()