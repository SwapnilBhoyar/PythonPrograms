"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 12:20:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-03 12:20:00
@Title : this program reverse the elements of array.
"""
from array import *
import logging

class ReverseOrderLogInfo:
    logging.basicConfig(filename="ReverseOrderLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)
    
class ReverseOrder:
    def getReverse(self):
        """
        Description:
            function reverse the array
        """
        
        integerArray = array('i', [10,20,30,40,50])
        
        res_arr=array('i',reversed(integerArray))
        print("Resultant Reversed Array:",res_arr)

if __name__ == "__main__":
    reverseOrder = ReverseOrder()
    try:
        reverseOrder.getReverse()
    except Exception as e:
        ReverseOrderLogInfo.logger.error(e)