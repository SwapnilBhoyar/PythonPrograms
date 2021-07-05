"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 17:54:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 17:54:00
@Title : Write a Python program to remove a key from a dictionary.
"""
from Log import Log
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
    Log.logger.error(e)
