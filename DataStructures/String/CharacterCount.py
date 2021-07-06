"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 20:08:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 20:08:00
@Title : Write a Python program to count the number of characters (character frequency) in a
string.
"""
from Log import Log

def characterCount():
    """
    Description:
        this function gives character count 
    """
    nameString = "hello how are you"
    charFrequency = {}
    
    for char in nameString:
        if char in charFrequency:
            charFrequency[char] += 1
        else:
            charFrequency[char] = 1

    Log.logger.info(charFrequency)

characterCount()

