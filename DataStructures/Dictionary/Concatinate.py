"""
@Author: Swapnil Bhoyar
@Date: 2021-07-04 15:19:00
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-07-04 15:19:00
@Title : this program concatinate dictionary.
"""
from Log import Log
    
class Concatinate:
    """
    Description:
        this function concatinate dictionary
    """
    def getConcatinate(self):
        firstDict={1:10, 2:20}
        secondDict={3:30, 4:40}
        thirdDict={5:50,6:60}
        fourthDict = {}
        for dictionary in (firstDict, secondDict, thirdDict): fourthDict.update(dictionary)
        print(fourthDict)

if __name__=="__main__":
    Concatinate = Concatinate()
    try:
        Concatinate.getConcatinate()
    except Exception as e:
        Log.logger.error(e)