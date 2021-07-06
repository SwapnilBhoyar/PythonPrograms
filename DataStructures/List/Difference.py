"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 09:28:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 09:28:00
@Title : Write a Python program to get the difference between the two lists
"""
from os import name
from Log import Log

class Difference:
    def getDifference(self):
        """
        Description:
            this function calcutate difference
        """
        firstNumberList = [12, 14, 16, 18]
        secondNumberList = [11, 12, 13, 14]

        differenceList = list(set(firstNumberList) - set(secondNumberList)) +list(set(secondNumberList) - set(firstNumberList))

        Log.logger.info(differenceList)

if __name__=="__main__":
    difference = Difference()
    try:
        difference.getDifference()
    except Exception as e:
        Log.logger.error(e)