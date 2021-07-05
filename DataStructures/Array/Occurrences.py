"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 2:13:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-03 2:13:00
@Title : this program reverse the elements of array.
"""
from array import *
from Log import Log

class Occurences:
    """
    Description:
        this function count occurences of a number
    """
    def getCount(self):
        count = 0
        occurenceOf = 20
        integerArray = array('i', [10,20,30,40,50,20])

        for element in integerArray:
            if(element == occurenceOf):
                count += 1

        print(count)

if __name__ == "__main__":
    occurences = Occurences()
    try:
        occurences.getCount()
    except Exception as e:
        Log.logger.error(e)