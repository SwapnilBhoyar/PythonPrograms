"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 11:24:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-06 11:24:00
@Title : Write a Python program to remove duplicates from a list of lists.
"""
from Log import Log
class ListOfList:
    def getRemoveDuplicate(self):
        """
        Description:
            this function remove duplicate sublist
        """
        testList = [[1, 0, -1], [-1, 0, 1], [-1, 0, 1],
                                [1, 2, 3], [3, 4, 1]]
        
        result = list(set(tuple(sorted(subList)) for subList in testList))
        
        Log.logger.info(result)

if __name__=="__main__":
    listOfList = ListOfList()
    try:
        listOfList.getRemoveDuplicate()
    except Exception as e:
        Log.logger.error(e)