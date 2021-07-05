"""
@Author: Swapnil Bhoyar
@Date: 2021-07-05 21:04:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 21:04:00
@Title : Write a Python program to get the smallest number from a list.
"""
from Log import Log
class SmallestNumber:
    def getSmallestNumber(self):
        numberList = ([2, 6, 9, 1, 3])
        minimumNumber = numberList[0]
        for number in numberList:
            if number < minimumNumber:
                minimumNumber = number

        Log.logger.info(minimumNumber)

if __name__=="__main__":
    smallestNumber = SmallestNumber()
    try:
        smallestNumber.getSmallestNumber()
    except Exception as e:
        Log.logger.error(e)