"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 09:41:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 09:41:00
@Title : Write a Python program to append a list to the second list.
"""
from Log import Log
class AppendList:
    def getApendList(self):
        """
        Description:
            this function concatinate two list
        """
        numberList = [1, 2, 3]
        stringList = ['five', 'six', 'seven']

        resultList = numberList + stringList
        Log.logger.info(resultList)

if __name__=="__main__":
    appendList = AppendList()
    try:
        appendList.getApendList()
    except Exception as e:
        Log.logger.error(e)