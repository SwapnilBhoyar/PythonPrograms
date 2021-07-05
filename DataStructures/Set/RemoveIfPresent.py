"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 01:27:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 01:27:00
@Title : Write a Python program to remove an item from a set if it is present in the set.
"""
from Log import Log

class RemoveIfPresent:
    def getRemoveIfPresent(self):
        """
        Description:
            this function remove element if present
        """
        numSet = set([0, 1, 2, 3, 4, 5])
        print("Original set elements:")
        print(numSet)

        numSet.discard(4)
        print(numSet)
        numSet.discard(5)
        print(numSet)
        numSet.discard(5)
        print(numSet)
        numSet.discard(15)
        print(numSet)

if __name__=="__main__":
    removeIfPresent = RemoveIfPresent()
    try:
        removeIfPresent.getRemoveIfPresent()
    except Exception as e:
        Log.logger.error(e)