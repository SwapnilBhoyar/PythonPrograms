"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 00:20:00
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-03 00:20:00
@Title : this program dispaly the elements of array.
"""
from array import *
import logging

class ArrayOfIntegersLog:
    logging.basicConfig(filename="ArrayOfIntegersLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class ArrayOfIntegers:
    def getArray(self):
        """
        Description:
            function display array
        """
    
        integerArray = array('i', [10,20,30,40,50])

        print(integerArray[0])
        print(integerArray[1])
        print(integerArray[2])
        print(integerArray[3])
        print(integerArray[4])

if __name__ == "__main__":

    arrayOfIntegers = ArrayOfIntegers()
    try:
        arrayOfIntegers.getArray()
    except Exception as e:
        ArrayOfIntegersLog.logger.error(e)