"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 17:54:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 17:54:00
@Title : Write a Python program to remove a key from a dictionary.
"""
import logging

class RemoveKeyLog:
    logging.basicConfig(filename="RemoveKeyLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
    #Creating an object
    logger=logging.getLogger()
    
    #Setting the threshold of logger to ERROR
    logger.setLevel(logging.ERROR)

class RemoveKey:
    """
    Description:
        this function remove key from dictionary
    """
    def getRemoveKey(self):
        dictionary = {'a':1,'b':2,'c':3,'d':4}
        print(dictionary)
        if 'a' in dictionary: 
            del dictionary['a']
        print(dictionary)

removeKey = RemoveKey()
try:
    removeKey.getRemoveKey()
except Exception as e:
    RemoveKeyLog.logger.error(e)
