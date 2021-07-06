"""
@Author: Swapnil Bhoyar
@Date: 2021-07-05 10:19:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 10:19:00
@Title : Write a Python program to find maximum and the minimum value in a set.
"""
from Log import Log

class MinMax:
    def getMinMax(self):
        """
        Description:
            this function calculate min and max element
        """
        numberSet = {5, 10, 3, 15, 2, 20}
        print("Original set elements:")
        print(numberSet)
       
        print("\nMaximum value of the said set:")
        print(max(numberSet))

        print("\nMinimum value of the said set:")
        print(min(numberSet))

        number = {3}
        print(type(number))

if __name__=="__main__":
    minMax = MinMax()
    try:
        minMax.getMinMax()
    except Exception as e:
        Log.logger.error(e)