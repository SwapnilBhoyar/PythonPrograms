"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 01:58:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 01:58:00
@Title : Write a Python program to find the list of words that are longer than n from a
given list of words.
"""
from Log import Log

class StringGreaterThanN:
    def getStringGreaterThanN(self):
        """
        Description:
            this function give string length greater than N
        """
        stringList = ['hello', 'my', 'name', 'is', 'swapnil']
        resultList = []
        N = 2

        for item in stringList:
            if len(item) > N:
                resultList.append(item)

        Log.logger.info(resultList)

if __name__=="__main__":
    stringGreaterThanN = StringGreaterThanN()
    try:
        stringGreaterThanN.getStringGreaterThanN()
    except Exception as e:
        Log.logger.error(e)