"""
@Author: Swapnil Bhoyar
@Date: 2021-07-05 22:06:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 22:06:00
@Title : Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings.
"""
from Log import Log

class CountStrings:
    def getCountString(self):
        """
        Description:
            this function count the number of strings.
        """
        count = 0

        stringList = (['abc', 'xyz', 'aba', '1221'])
        for word in stringList:
            if len(word) > 1 and word[0] == word[-1]:
                count += 1
        Log.logger.info(count)

if __name__=="__main__":
    countStrings = CountStrings()
    try:
        countStrings.getCountString()
    except Exception as e:
        Log.logger.error(e)