"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 00:20:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-03 00:20:00
@Title : this program dispaly the elements of array.
"""
from array import *
from Log import Log

class ArrayOfIntegers:
    def getArray(self):
        """
        Description:
            function display array
        """
    
        integerArray = array('i', [10,20,30,40,50])

        Log.logger.info(integerArray[0])
        Log.logger.info(integerArray[1])
        Log.logger.info(integerArray[2])
        Log.logger.info(integerArray[3])
        Log.logger.info(integerArray[4])

if __name__ == "__main__":

    arrayOfIntegers = ArrayOfIntegers()
    try:
        arrayOfIntegers.getArray()
    except Exception as e:
        Log.logger.error(e)