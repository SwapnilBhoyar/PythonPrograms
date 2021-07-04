"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 00:52:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 00:52:00
@Title : Write a Python program to remove item(s) from a given set.
"""
import logging

class RemoveElementLog:
    logging.basicConfig(filename="RemoveElementLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

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
    RemoveElementLog.logger.error(e)