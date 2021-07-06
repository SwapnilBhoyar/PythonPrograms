"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 10:42:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-06 10:42:00
@Title : Write a Python program to split a list based on first character of word.
"""
from Log import Log

class SplitString:
    def getSplitString(self):
        """
        Descrption:
            this function split geiven string
        """
        name = 'Swapnil'
        resultName = list(name)
        Log.logger.info(resultName)

if __name__=="__main__":
    splitString = SplitString()
    try:
        splitString.getSplitString()
    except Exception as e:
        Log.logger.error(e)