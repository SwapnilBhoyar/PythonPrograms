"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 15:00:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 15:00:00
@Title : this program add key to dictionary.
"""
from array import *
import logging

class AddKeyLog:
    logging.basicConfig(filename="AddKeyLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class AddKey:
    def add(self):
        """
        Description:
            this function add key to dictionary.
        """
        intDictionary = {0:10, 1:20}
        print(intDictionary)
        intDictionary.update({2:30})
        print(intDictionary)

if __name__=="__main__":
    addKey = AddKey()
    addKey.add()