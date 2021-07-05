"""
@Author: Swapnil Bhoyar
@Date: 2021-07-06 02:16:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-05 02:16:00
@Title : Write a Python function that takes two lists and returns True if they have at
least one common member.
"""
from Log import Log

class CommonMember:
    def getCommonMember(self, firstList, secondList):
        """
        Description:
            this function return true if common element is in liats
        """
        result = False

        for firstListItem in firstList:
            for secondListItem in secondList:
                if firstListItem == secondListItem:
                    result = True

        Log.logger.info(result)

if __name__=="__main__":
    commonMember = CommonMember()
    try:
        firstList = [11, 23, 43, 50, 119, 56]
        secondList = [21, 34, 11, 32]
        commonMember.getCommonMember(firstList, secondList)
    except Exception as e:
        Log.logger.error(e)
