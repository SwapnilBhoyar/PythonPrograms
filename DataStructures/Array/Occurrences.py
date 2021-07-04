"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 2:13:00
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-07-03 2:13:00
@Title : this program reverse the elements of array.
"""
from array import *
import logging

class OccurencesLog:
    logging.basicConfig(filename="OccurencesLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

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
        OccurencesLog.logger.error(e)