"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 17:47:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 17:47:00
@Title : Write a Python program to find the repeated items of a tuple.
"""

from Log import Log

def repeatedElement():
    """
    Description:
        this function find duplicate element
    """
    numberSet = set([])
    tupple = (1,3,4,32,1,1,1,31,32,12,21,2,3) 
    #count() count number of times repeatation of a value 
    for number in tupple:
        if tupple.count(number) > 1:
            numberSet.add(number)
        check = 4 in tupple #return true or false
    Log.logger.info(numberSet)
    Log.logger.info(check)


repeatedElement()