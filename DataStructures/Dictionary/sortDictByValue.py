"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 2:13:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 11:29:00
@Title : this program remove the elements of array.
"""
from array import *
import logging
import operator

class SortDictByValueLog:
    logging.basicConfig(filename="SortDictByValueLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class SortDictByValue:
    def sortDictionary(self):
        intDictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
        print('Original dictionary : ',intDictionary)

        ascDictionary = sorted(intDictionary.items(), key=operator.itemgetter(1))
        print('Dictionary in ascending order by value : ',ascDictionary)

        desDictionary = dict( sorted(intDictionary.items(), key=operator.itemgetter(1),reverse=True))
        print('Dictionary in descending order by value : ',desDictionary)

if __name__=="__main__":
    soryDictByValue = SortDictByValue()
    try:
        soryDictByValue.sortDictionary()
    except Exception as e:
        SortDictByValueLog.logger.error(e)