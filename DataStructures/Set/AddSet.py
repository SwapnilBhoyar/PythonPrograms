"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 00:41:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 00:41:00
@Title : Write a Python program to add member(s) in a set.
"""
from Log import Log
class AddSet:
    def checkAddSet(self):
        """
        Description
            this function add element to set
        """
        colorSet = set()
        print(colorSet)

        print("\nAdd single element:")
        colorSet.add("Red")
        print(colorSet)

        print("\nAdd multiple items:")
        colorSet.update(["Blue", "Green"])
        print(colorSet)

        number = set([])

if __name__=="__main__":
    addSet = AddSet()
    try:
        addSet.checkAddSet()
    except Exception as e:
        Log.logger.error(e)