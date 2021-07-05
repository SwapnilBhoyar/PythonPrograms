"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 01:23:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 01:23:00
@Title : Write a Python program to remove duplicates from a list.
"""
from Log import Log

class RemoveDuplicate:
    def getRemoveDuplicate(self):
        """
        Description:
            this function remove dublicate elemenrts
        """
        numberList = [1, 5, 8, 7, 1, 6, 5, 7]
        resultList = []
        for number in numberList:
            if number not in resultList:
                resultList.append(number)

        Log.logger.info(resultList)

if __name__=="__main__":
    removeDuplicate = RemoveDuplicate()
    try:
        removeDuplicate.getRemoveDuplicate()
    except Exception as e:
        Log.logger.error(e)