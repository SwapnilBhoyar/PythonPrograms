"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 2:13:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 11:29:00
@Title : this program remove the elements of array.
"""
from array import *

from Log import Log

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
        Log.logger.error(e)