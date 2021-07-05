"""
@Author: Swapnil Bhoyar
@Date: 2021-07-05 09:29:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 02:29:00
@Title : Write a Python program to clear a set.
"""
from Log import Log
class ClearSet:
    def getClearSet(self):
        """
        Description:
            this function clear the set
        """
        setc = {"Red", "Green", "Black", "White"}
        print("Original set elements:")
        print(setc)  

        print("\nAfter removing all elements of the said set.")
        setc.clear()
        print(setc)

if __name__=="__main__":
    clearSet = ClearSet()
    try:
        clearSet.getClearSet()
    except Exception as e:
        Log.logger.error(e)