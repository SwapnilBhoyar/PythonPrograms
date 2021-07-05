"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 19:59:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 19:59:00
@Title : Write a Python program to convert a list into a nested dictionary of keys.
"""
from Log import Log

class ListToDictionary:
    def getListToDictionary(self):
        """
        Description:
            this function convert list to nested dictionary"""
        numberList = [1, 2, 3, 4]
        newDictionary = current = {}
        for name in numberList:
            current[name] = {}
            current = current[name]
        print(newDictionary)

if __name__=="__main__":
    listToDictionary = ListToDictionary()
    try:
        listToDictionary.getListToDictionary()
    except Exception as e:
        Log.logger.error(e)