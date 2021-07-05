"""
@Author: Swapnil Bhoyar
@Date: 2021-07-05 20:40:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 20:40:00
@Title : Write a Python program to multiplication all the items in a list..
"""
from Log import Log

class MulOfItems:
    """
    Description:
        this function calculate multiplication of list element
    """
    def getMulOfItems(self):
        MUL = 1
        numberList = ([1, 3, 5, 6])

        for number in numberList:
            MUL *= number
        Log.logger.info(MUL)

if __name__=="__main__":
    mulOfItems = MulOfItems()

    try:
        mulOfItems.getMulOfItems()
    except Exception as e:
        Log.logger.error(e)