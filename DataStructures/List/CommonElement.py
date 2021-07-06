"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 10:21:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-06 10:21:00
@Title : Write a Python program to find common items from two lists.
"""
from Log import Log
class CommonElement:
    def getCommonElement(self):
        """
        Description:
            this function identify common elements
        """
        firstNumberList = [11, 12, 13, 14, 15]
        secondNumberList = [13, 14, 15, 16, 17]
        resultList = []

        for firstNumber in firstNumberList:
            for secondNumber in secondNumberList:
                if firstNumber == secondNumber:
                    resultList.append(firstNumber)

        Log.logger.info(resultList)

if __name__=="__main__":
    commonElement = CommonElement()
    try:
        commonElement.getCommonElement()
    except Exception as e:
        Log.logger.error(e)