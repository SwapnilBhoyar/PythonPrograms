"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 22:50:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 22:50:00
@Title : Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of thegiven string is less than 3, leave it unchanged.
"""

from Log import Log

def addIng(tempString):
    """
    Description:
    this function add ing or ly 
    """
    length = len(tempString)
    if length > 2:  
        if tempString[-3:] == 'ing':
            tempString += 'ly'
        else:
            tempString += 'ing'

    Log.logger.info(tempString)

addIng('ab')
addIng('abc')
addIng('string')
