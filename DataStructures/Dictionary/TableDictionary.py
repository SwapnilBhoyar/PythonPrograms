"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 18:12:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 18:12:00
@Title : Write a Python program to print a dictionary in table format.
"""
from Log import Log

class TableDictionary:
    """
    Description:
        this function write dictionary in table format
    """
    def getTableDictionary(self):
        dictionary = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
        for row in zip(*([key] + (value) for key, value in sorted(dictionary.items()))):
            print(*row)

if __name__=="__main__":
    tableDictionary = TableDictionary()
    try:
        tableDictionary.getTableDictionary()
    except Exception as e:
        Log.logger.error(e)