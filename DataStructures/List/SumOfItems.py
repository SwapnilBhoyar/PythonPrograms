"""
@Author: Swapnil Bhoyar
@Date: 2021-07-05 20:40:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 20:40:00
@Title : Write a Python program to SUM all the items in a list..
"""
from Log import Log

class SumOfItems:
    """
    Description:
        this function calculate SUM of list element
    """
    def getSumOfItems(self):
        SUM = 0
        numberList = ([1, 3, 5, 6])

        for number in numberList:
            SUM += number
        Log.logger.info(SUM)

if __name__=="__main__":
    sumOfItems = SumOfItems()

    try:
        sumOfItems.getSumOfItems()
    except Exception as e:
        Log.logger.error(e)