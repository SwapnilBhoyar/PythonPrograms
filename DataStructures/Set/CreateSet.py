"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 23:39:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 23:39:00
@Title : Write a Python program to create a set.
"""
from Log import Log

class CreateSet:
    def getSet(self):
        """
        Description:
            this function contains set
        """
        intSet = set([0, 1, 2, 3, 4])
        print(intSet)

        mixSet = {1,2,3,'foo','bar'}
        print(mixSet)

if __name__=="__main__":
    createSet = CreateSet()
    try:
        createSet.getSet()
    except Exception as e:
            Log.logger.error(e)