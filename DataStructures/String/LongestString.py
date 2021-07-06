"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 22:50:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 22:50:00
@Title : Write a Python function that takes a list of words and returns the length of the longest
one"""

from Log import Log

def longestString():
    """
    Description:
        this function longest string length
    """
    stringList = ["Swapnil", "Sanjay", "Aditya"]
    wordLength = []
    for string in stringList:
        temp = wordLength.append(len(string))
    temp2 = wordLength.sort()
    Log.logger.info(wordLength[-1])

longestString()
