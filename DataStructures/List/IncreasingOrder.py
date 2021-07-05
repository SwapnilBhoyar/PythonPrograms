"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 01:08:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 01:08:00
@Title : Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
"""
from Log import Log

class IncreasingOrder:
    def getIncreasingOrder(self): 
        """
        Description:
            this function convert list in increasing order base on second tuple
        """ 
        valueList =[(1, 11), (3, 9), (2, 5)]
        # getting length of list of tuples 
        length = len(valueList)  
        for i in range(0, length):  
                
            for j in range(0, length-i-1):  
                if (valueList[j][-1] > valueList[j + 1][-1]):  
                    temp = valueList[j]  
                    valueList[j]= valueList[j + 1]  
                    valueList[j + 1]= temp  
        Log.logger.info(valueList)

if __name__=="__main__":
    increasingOrder = IncreasingOrder()
    try:
        increasingOrder.getIncreasingOrder()
    except Exception as e:
        Log.logger.error(e)
          


