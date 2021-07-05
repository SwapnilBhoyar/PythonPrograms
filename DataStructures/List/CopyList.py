"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 01:39:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 01:39:00
@Title : Write a Python program to clone or copy a list.
"""
from Log import Log

class CopyList:
    def getCopyList(self):
        """
        Description:
            this function create copy of list
         """
        numberList = [2, 4, 6, 8]
        resultList = numberList[ : ]

        Log.logger.info(resultList)

if __name__=="__main__":
    copyList = CopyList()
    try:
        copyList.getCopyList()
    except Exception as e:
        Log.logger.error(e)