"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 02:16:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 02:16:00
@Title : Write a Python function that takes two lists and returns True if they have at
least one common member.
"""
from Log import Log

class RemoveFromList:
    def getRemoveFromList(self):
        """
        Description:
            this function remove element from list
        """
        FIRST = 0
        FOURTH = 3
        FIFTH = 3
        stringList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

        del stringList[FIRST]
        del stringList[FOURTH]
        del stringList[FIFTH]

        Log.logger.info(stringList)

if __name__=="__main__":
    removeFromList = RemoveFromList()
    try:
        removeFromList.getRemoveFromList()
    except Exception as e:
        Log.logger.error(e)