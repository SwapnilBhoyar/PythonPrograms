"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 2:13:00
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-04 11:29:00
@Title : this program remove the elements of array.
"""
from array import *
import logging

class RemoveElementLog:
    logging.basicConfig(filename="RemoveElementLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

from array import *
class RemoveElement:
    """
    Description:
        this function remove element from array
    """
    def remove(self):
        integerArray = array('i', [10,20,30,40,50,20])
        integerArray.remove(20)
        print(integerArray)

if __name__=="__main__":
    removeElement = RemoveElement()
    try:
        removeElement.remove()
    except Exception as e:
        RemoveElementLog.logger.error(e)