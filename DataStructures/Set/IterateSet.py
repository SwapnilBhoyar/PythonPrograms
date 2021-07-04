"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 00:23:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 00:23:00
@Title : Write a Python program to iteration over sets.
"""
import logging

class IterateSetLog:
    logging.basicConfig(filename="IterateSetLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class IterateSet:
    def checkIterateSet(self):
        """
        description:
            this function iterate over set
        """
        num_set = set([0, 1, 2, 3, 4, 5])
        for element in num_set:
            print(element, end=' ')

if __name__=="__main__":
    iterateSet = IterateSet()
    try:
        iterateSet.checkIterateSet()
    except Exception as e:
        IterateSetLog.logger.error(e)
