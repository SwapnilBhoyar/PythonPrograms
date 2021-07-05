"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 00:52:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 00:52:00
@Title : Write a Python program to remove item(s) from a given set.
"""
from Log import Log

class RemoveElement:
    def getRemoveElement(self):
        """
        Description:
            this function remove element
        """
        intSet = set([0, 1, 3, 4, 5])
        print("Original set:")
        print(intSet)
        intSet.pop()
        print("\nAfter removing the first element from the said set:")
        print(intSet)

removeElement = RemoveElement()
try:
    removeElement.getRemoveElement()
except Exception as e:
    Log.logger.error(e)